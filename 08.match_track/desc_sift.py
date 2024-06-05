import cv2
import numpy as np

def main(image_path):
    # 이미지 읽기
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    # 그레이스케일로 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # SIFT 추출기 생성
    try:
        sift = cv2.xfeatures2d.SIFT_create()
    except AttributeError:
        print("Error: SIFT is not available in your OpenCV version. Please ensure you have the contrib modules installed.")
        return

    # 키 포인트 검출과 서술자 계산
    keypoints, descriptors = sift.detectAndCompute(gray, None)
    
    if descriptors is not None:
        print(f'Keypoints: {len(keypoints)}, Descriptor shape: {descriptors.shape}')
    else:
        print("Error: No descriptors found.")
        return

    # 키 포인트 그리기
    img_draw = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # 결과 출력
    cv2.imshow('SIFT', img_draw)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = '../img/house.jpg'
    main(image_path)
