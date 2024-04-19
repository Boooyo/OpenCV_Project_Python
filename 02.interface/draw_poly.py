import cv2
import numpy as np

def draw_polygon(img, pts, is_closed, color, thickness=1):
    cv2.polylines(img, [pts], is_closed, color, thickness)

def main():
    img = cv2.imread('../img/blank_500.jpg')

    # 다각형의 좌표 배열 정의
    polygons = [
        (np.array([[50,50], [150,150], [100,140],[200,240]], dtype=np.int32), False, (255,0,0)), # 번개 모양 선
        (np.array([[350,50], [250,200], [450,200]], dtype=np.int32), False, (0,0,0)),             # 삼각형
        (np.array([[150,300], [50,450], [250,450]], dtype=np.int32), True, (0,0,255)),            # 삼각형 (닫힌 도형)
        (np.array([[350,250], [450,350], [400,450], [300,450], [250,350]], dtype=np.int32), True, (0,0,0)) # 5각형
    ]

    # 다각형 그리기
    for pts, is_closed, color in polygons:
        draw_polygon(img, pts, is_closed, color, thickness=10 if is_closed else 1)

    cv2.imshow('polyline', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
