import cv2
import numpy as np

# 이미지 읽기
img = cv2.imread('../img/bad_rect.png')
img2 = img.copy()

# 그레이스케일로 변환
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 바이너리 스케일 변환
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)

# 컨투어 찾기
contours, hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 첫 번째 컨투어 선택
contour = contours[0]

# 전체 둘레의 0.05로 오차 범위 지정
epsilon = 0.05 * cv2.arcLength(contour, True)

# 근사 컨투어 계산
approx = cv2.approxPolyDP(contour, epsilon, True)

# 각각 컨투어 선 그리기
cv2.drawContours(img, [contour], -1, (0, 255, 0), 3)
cv2.drawContours(img2, [approx], -1, (0, 255, 0), 3)

# 결과 출력
cv2.imshow('Original Contour', img)
cv2.imshow('Approximated Contour', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
