import numpy as np
import cv2

def detect_faces_and_eyes(image_path):
    # 얼굴 검출을 위한 케스케이드 분류기 생성
    face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
    # 눈 검출을 위한 케스케이드 분류기 생성
    eye_cascade = cv2.CascadeClassifier('./data/haarcascade_eye.xml')
    
    # 이미지 읽기 및 그레이 스케일 변환
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 얼굴 검출
    faces = face_cascade.detectMultiScale(gray)
    
    # 검출된 얼굴 순회
    for (x, y, w, h) in faces:
        # 검출된 얼굴에 사각형 표시
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # 얼굴 영역을 ROI로 설정
        roi_gray = gray[y:y+h, x:x+w]
        
        # ROI에서 눈 검출
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        # 검출된 눈에 사각형 표시
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(img, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)
    
    # 결과 출력
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 함수 호출하여 이미지에서 얼굴과 눈 검출
detect_faces_and_eyes('../img/children.jpg')
