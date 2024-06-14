import cv2

# 캐스케이드 분류기 경로
CASCADE_PATH_FACE = '../data/haarcascade_frontalface_default.xml'
CASCADE_PATH_EYE = '../data/haarcascade_eye.xml'

# 상수 정의
SCALE_FACTOR = 1.3
MIN_NEIGHBORS = 5
MIN_SIZE = (80, 80)
MAX_EYES = 2

def detect_faces_and_eyes(frame, face_cascade, eye_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 얼굴 검출
    faces = face_cascade.detectMultiScale(gray, scaleFactor=SCALE_FACTOR, minNeighbors=MIN_NEIGHBORS, minSize=MIN_SIZE)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        
        # 눈 검출
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for i, (ex, ey, ew, eh) in enumerate(eyes):
            if i >= MAX_EYES:
                break
            cv2.rectangle(frame, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (255, 0, 0), 2)
    
    return frame

def main():
    # 캐스케이드 분류기 생성
    face_cascade = cv2.CascadeClassifier(CASCADE_PATH_FACE)
    eye_cascade = cv2.CascadeClassifier(CASCADE_PATH_EYE)
    
    # 카메라 캡쳐 활성화
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = detect_faces_and_eyes(frame, face_cascade, eye_cascade)
        
        cv2.imshow('Face Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == 27:  # ESC 키 누르면 종료
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
