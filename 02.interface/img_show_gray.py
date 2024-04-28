import cv2

def show_grayscale_image(img_file):
    img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
    if img is not None:
        cv2.imshow('Grayscale Image', img)
        cv2.waitKey()
        cv2.destroyAllWindows()
    else:
        print('No image file.')

if __name__ == "__main__":
    img_file = "../img/yeosu.jpg"
    show_grayscale_image(img_file)
