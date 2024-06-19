import cv2
import numpy as np

def preprocess_image(image_path):
    """이미지를 읽고 그레이 스케일 및 바이너리 스케일로 변환"""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("이미지를 불러올 수 없습니다.")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    return img, th

def find_and_draw_contours(img, binary_img):
    """컨투어를 찾고 이미지를 복사하여 컨투어를 그립니다."""
    contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0:
        raise ValueError("컨투어를 찾을 수 없습니다.")
    contour = contours[0]
    img_contour = img.copy()
    cv2.drawContours(img_contour, [contour], -1, (0, 255, 0), 1)
    return contour, img_contour

def draw_convex_hull(img, contour):
    """볼록 선체를 그리고 이미지를 복사하여 그립니다."""
    hull = cv2.convexHull(contour)
    img_hull = img.copy()
    cv2.drawContours(img_hull, [hull], -1, (0, 255, 0), 1)
    return hull, img_hull

def find_and_draw_convexity_defects(img, contour, hull):
    """볼록 선체 결함을 찾고, 결함을 원으로 표시합니다."""
    hull_indices = cv2.convexHull(contour, returnPoints=False)
    defects = cv2.convexityDefects(contour, hull_indices)
    img_defects = img.copy()

    if defects is not None:
        for i in range(defects.shape[0]):
            start_index, end_index, farthest_index, distance = defects[i, 0]
            farthest_point = tuple(contour[farthest_index][0])
            dist = distance / 256.0

            if dist > 1:
                cv2.circle(img_defects, farthest_point, 3, (0, 0, 255), -1)
    
    return img_defects

def main():
    image_path = '../img/hand.jpg'
    
    # 이미지 전처리
    img, binary_img = preprocess_image(image_path)

    # 컨투어 찾기와 그리기
    contour, img_contour = find_and_draw_contours(img, binary_img)

    # 볼록 선체 찾기와 그리기
    hull, img_hull = draw_convex_hull(img, contour)

    # 볼록 선체 만족 여부 확인
    print("Is original contour convex:", cv2.isContourConvex(contour))
    print("Is convex hull convex:", cv2.isContourConvex(hull))

    # 볼록 선체 결함 찾기와 그리기
    img_defects = find_and_draw_convexity_defects(img_hull, contour, hull)

    # 결과 이미지 표시
    cv2.imshow('Contour', img_contour)
    cv2.imshow('Convex Hull', img_hull)
    cv2.imshow('Convexity Defects', img_defects)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
