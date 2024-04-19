import cv2

def draw_rectangles(img, rectangles):
    for rect in rectangles:
        cv2.rectangle(img, rect[0], rect[1], rect[2], rect[3])

def main():
    img = cv2.imread('../img/blank_500.jpg')

    # 사각형의 좌표와 속성 배열로 정의
    rectangles = [
        ((50, 50), (150, 150), (255,0,0), 1),     # 좌상, 우하 좌표로 사각형 그리기
        ((300, 300), (100, 100), (0,255,0), 10),  # 우하, 좌상 좌표로 사각형 그리기
        ((450, 200), (200, 450), (0,0,255), -1)   # 우상, 좌하 좌표로 사각형 채워 그리기
    ]

    # 사각형 그리기
    draw_rectangles(img, rectangles)

    cv2.imshow('rectangle', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
