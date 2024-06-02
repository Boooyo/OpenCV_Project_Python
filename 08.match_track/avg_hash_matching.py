import cv2
import numpy as np
import glob

def display_image(window_name, img):
    # 지정된 창에 이미지를 표시합니다.
    cv2.imshow(window_name, img)
    cv2.waitKey(5)

def img2hash(img, hash_size=16):
    # 이미지를 해시로 변환합니다.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (hash_size, hash_size))
    avg = gray.mean()
    bi = 1 * (gray > avg)
    return bi

def hamming_distance(a, b):
    # 해밍 거리를 계산합니다.
    a = a.reshape(-1)
    b = b.reshape(-1)
    distance = np.count_nonzero(a != b)
    return distance

def main(query_img_path, search_dir, hash_size=16, threshold=0.25):
    # 쿼리 이미지 읽기 및 해시 계산
    query_img = cv2.imread(query_img_path)
    display_image('query', query_img)
    query_hash = img2hash(query_img, hash_size)

    # 검색 디렉토리의 모든 이미지 파일 경로
    img_paths = glob.glob(search_dir + '/**/*.jpg', recursive=True)
    
    for path in img_paths:
        # 데이터셋 이미지 읽기 및 해시 계산
        img = cv2.imread(path)
        display_image('searching...', img)
        a_hash = img2hash(img, hash_size)
        
        # 해밍 거리 계산
        dst = hamming_distance(query_hash, a_hash)
        
        if dst / (hash_size * hash_size) < threshold:
            print(path, dst / (hash_size * hash_size))
            display_image(path, img)
    
    cv2.destroyWindow('searching...')
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 주어진 이미지 파일 경로와 검색 디렉토리
query_img_path = '../img/pistol.jpg'
search_dir = '../img/101_ObjectCategories'

# 메인 함수 실행
main(q
