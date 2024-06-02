import cv2
import numpy as np

def compute_dhash(image_path, hash_size=16):
    # 이미지 읽고 그레이 스케일로 변환
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 8x8 크기로 축소
    resized_gray = cv2.resize(gray, (hash_size, hash_size))

    # 영상의 평균값 구하기
    avg = resized_gray.mean()

    # 평균값을 기준으로 0과 1로 변환
    bin_img = (resized_gray > avg).astype(int)

    # 2진수 문자열을 16진수 문자열로 변환
    dhash = ''.join(f'{int("".join(map(str, row)), 2):02x}' for row in bin_img)

    return dhash

def display_image(window_name, image_path):
    # 이미지 읽기
    img = cv2.imread(image_path)
    cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 주어진 이미지 파일 경로
image_path = '../img/pistol.jpg'

# 해시값 계산
dhash_value = compute_dhash(image_path)
print(f'DHash: {dhash_value}')

# 이미지 디스플레이
display_image('pistol', image_path)
