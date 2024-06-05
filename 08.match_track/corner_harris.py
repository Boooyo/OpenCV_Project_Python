import cv2
import numpy as np

def detect_harris_corners(image_path, block_size=2, ksize=3, k=0.04, threshold=0.1):
    # 이미지 읽기
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")
    
    # 그레이스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 해리스 코너 검출
    corner_response = cv2.cornerHarris(gray, block_size, ksize, k)

    # 변화량 결과의 최대값 10% 이상의 좌표 구하기
    coord = np.where(corner_response > threshold * corner_response.max())
    coord = np.stack((coord[1], coord[0]), axis=-1)

    # 코너 좌표에 동그리미 그리기
    for x, y in coord:
        cv2.circle(img, (x, y), 5, (0, 0, 255), 1, cv2.LINE_AA)

    return img, corner_response

def normalize_corner_response(corner_response):
    # 변화량을 영상으로 표현하기 위해서 0~255로 정규화
    corner_norm = cv2.normalize(corner_response, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    return cv2.cvtColor(corner_norm, cv2.COLOR_GRAY2BGR)

def display_images(corner_norm, img):
    # 두 이미지를 병합하여 표시
    merged = np.hstack((corner_norm, img))
    cv2.imshow('Harris Corner', merged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    image_path = '../img/house.jpg'
    img, corner_response = detect_harris_corners(image_path)
    corner_norm = normalize_corner_response(corner_response)
    display_images(corner_norm, img)

if __name__ == "__main__":
    main()
