import cv2
import numpy as np

# 이미지 읽기
img = cv2.imread('../img/house.jpg')
if img is None:
    raise FileNotFoundError("이미지를 찾을 수 없습니다.")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# SURF 추출기 생성 ( 경계:1000, 피라미드:3, 서술자확장:True, 방향적용:True)
try:
    surf = cv2.xfeatures2d.SURF_create(1000, 3, 4, True, True)
except AttributeError:
    print("SURF 모듈을 찾을 수 없습니다. 'opencv-contrib-python' 패키지가 설치되어 있는지 확인하십시오.")
    exit()

# 키 포인트 검출 및 서술자 계산
keypoints, desc = surf.detectAndCompute(gray, None)
if desc is not None:
    print(f"Descriptor shape: {desc.shape}")
else:
    print("No descriptors found")

# 키포인트 이미지에 그리기
img_draw = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# 이미지 출력
cv2.imshow('SURF', img_draw)
cv2.waitKey(0)
cv2.destroyAllWindows()
