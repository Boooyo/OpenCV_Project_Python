import cv2

def draw_lines(img, points, color, thickness=1, line_type=cv2.LINE_8):
    for i in range(len(points) - 1):
        cv2.line(img, points[i], points[i+1], color, thickness, line_type)

def draw_diagonal(img, color, thickness=1):
    cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), color, thickness)

img = cv2.imread('../img/blank_500.jpg')

# 단일 색상 선 그리기
draw_lines(img, [(50, 50), (150, 50)], (255, 0, 0))
draw_lines(img, [(200, 50), (300, 50)], (0, 255, 0))
draw_lines(img, [(350, 50), (450, 50)], (0, 0, 255))

# 혼합 색상 선 그리기
draw_lines(img, [(100, 100), (400, 100)], (255, 255, 0), 10)
draw_lines(img, [(100, 150), (400, 150)], (255, 0, 255), 10)
draw_lines(img, [(100, 200), (400, 200)], (0, 255, 255), 10)
draw_lines(img, [(100, 250), (400, 250)], (200, 200, 200), 10)
draw_lines(img, [(100, 300), (400, 300)], (0, 0, 0), 10)

# 다양한 연결 유형 선 그리기
draw_lines(img, [(100, 350), (400, 400)], (0, 0, 255), 20, cv2.LINE_4)
draw_lines(img, [(100, 400), (400, 450)], (0, 0, 255), 20, cv2.LINE_8)
draw_lines(img, [(100, 450), (400, 500)], (0, 0, 255), 20, cv2.LINE_AA)

# 이미지 전체에 대각선 그리기
draw_diagonal(img, (0, 0, 255))

cv2.imshow('lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
