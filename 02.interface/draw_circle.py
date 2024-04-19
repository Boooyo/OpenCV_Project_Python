import cv2

def draw_circle(img, center, radius, color, thickness=-1):
    cv2.circle(img, center, radius, color, thickness)

def draw_ellipse(img, center, axes, angle, start_angle, end_angle, color):
    cv2.ellipse(img, center, axes, angle, start_angle, end_angle, color)

img = cv2.imread('../img/blank_500.jpg')

# 원 그리기
draw_circle(img, (150, 150), 100, (255, 0, 0))
draw_circle(img, (300, 150), 70, (0, 255, 0), 5)
draw_circle(img, (400, 150), 50, (0, 0, 255), -1)

# 타원 그리기
draw_ellipse(img, (50, 300), (50, 50), 0, 0, 360, (0, 0, 255))
draw_ellipse(img, (150, 300), (50, 50), 0, 0, 180, (255, 0, 0))
draw_ellipse(img, (200, 300), (50, 50), 0, 181, 360, (0, 0, 255))
draw_ellipse(img, (325, 300), (75, 50), 0, 0, 360, (0, 255, 0))
draw_ellipse(img, (450, 300), (50, 75), 0, 0, 360, (255, 0, 255))
draw_ellipse(img, (50, 425), (50, 75), 15, 0, 360, (0, 0, 0))
draw_ellipse(img, (200, 425), (50, 75), 45, 0, 360, (0, 0, 0))
draw_ellipse(img, (350, 425), (50, 75), 45, 0, 180, (0, 0, 255))
draw_ellipse(img, (400, 425), (50, 75), 45, 181, 360, (255, 0, 0))

cv2.imshow('circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
