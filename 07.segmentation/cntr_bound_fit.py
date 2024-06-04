import cv2
import numpy as np

# 이미지 읽기
img = cv2.imread("../img/lightning.png")

# 그레이스케일로 변환 및 바이너리 스케일 변환
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

# 컨투어 찾기
contours, hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour = contours[0]

# 감싸는 사각형 표시 (검정색)
x, y, w, h = cv2.boundingRect(contour)
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 3)

# 최소한의 사각형 표시 (초록색)
rect = cv2.minAreaRect(contour)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img, [box], -1, (0, 255, 0), 3)

# 최소한의 원 표시 (파랑색)
(x, y), radius = cv2.minEnclosingCircle(contour)
cv2.circle(img, (int(x), int(y)), int(radius), (255, 0, 0), 2)

# 최소한의 삼각형 표시 (분홍색)
ret, triangle = cv2.minEnclosingTriangle(contour)
cv2.polylines(img, [np.int32(triangle)], True, (255, 0, 255), 2)

# 최소한의 타원 표시 (노랑색)
ellipse = cv2.fitEllipse(contour)
cv2.ellipse(img, ellipse, (0, 255, 255), 3)

# 중심점을 통과하는 직선 표시 (빨강색)
[vx, vy, x, y] = cv2.fitLine(contour, cv2.DIST_L2, 0, 0.01, 0.01)
cols, rows = img.shape[1], img.shape[0]
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
cv2.line(img, (0, lefty), (cols - 1, righty), (0, 0, 255), 2)

# 결과 출력
cv2.imshow('Bound Fit Shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
