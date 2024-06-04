import cv2
import numpy as np

# 이미지 읽기
img = cv2.imread('../img/hand.jpg')
img2 = img.copy()

# 그레이 스케일 및 바이너리 스케일 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 컨투어 찾기와 그리기
contours, hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour = contours[0]
cv2.drawContours(img, [contour], -1, (0, 255, 0), 1)

# 볼록 선체 찾기(좌표 기준)와 그리기
hull = cv2.convexHull(contour)
cv2.drawContours(img2, [hull], -1, (0, 255, 0), 1)

# 볼록 선체 만족 여부 확인
print("Is original contour convex:", cv2.isContourConvex(contour))
print("Is convex hull convex:", cv2.isContourConvex(hull))

# 볼록 선체 찾기(인덱스 기준)
hull_indices = cv2.convexHull(contour, returnPoints=False)

# 볼록 선체 결함 찾기
defects = cv2.convexityDefects(contour, hull_indices)

# 볼록 선체 결함 순회
if defects is not None:
    for i in range(defects.shape[0]):
        start_index, end_index, farthest_index, distance = defects[i, 0]
        farthest_point = tuple(contour[farthest_index][0])
        dist = distance / 256.0
        
        if dist > 1:
            cv2.circle(img2, farthest_point, 3, (0, 0, 255), -1)

# 결과 이미지 표시
cv2.imshow('Contour', img)
cv2.imshow('Convex Hull', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
