import cv2
import numpy as np

def load_image(image_path):
    # 이미지를 읽어들입니다.
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")
    return img

def convert_to_gray(img):
    # 이미지를 그레이스케일로 변환합니다.
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def detect_and_compute_orb(img):
    # ORB 추출기를 생성하고 키 포인트와 서술자를 계산합니다.
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(img, None)
    return keypoints, descriptors

def draw_keypoints(img, keypoints):
    # 이미지에 키 포인트를 그립니다.
    return cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

def display_image(winname, img):
    # 이미지를 화면에 출력합니다.
    cv2.imshow(winname, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    image_path = '../img/house.jpg'
    img = load_image(image_path)
    gray_img = convert_to_gray(img)
    keypoints, descriptors = detect_and_compute_orb(gray_img)
    img_with_keypoints = draw_keypoints(img, keypoints)
    display_image('ORB', img_with_keypoints)

if __name__ == "__main__":
    main()
