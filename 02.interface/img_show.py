import cv2

class ImageViewer:
    def __init__(self, img_file):
        self.img_file = img_file

    def show_image(self):
        img = cv2.imread(self.img_file)
        if img is not None:
            cv2.imshow('Image Viewer', img)
            cv2.waitKey()
            cv2.destroyAllWindows()
        else:
            print('No image file.')

if __name__ == "__main__":
    img_file = "../img/yeosu.jpg"
    image_viewer = ImageViewer(img_file)
    image_viewer.show_image()
