import cv2

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), 30, (0, 0, 0), -1)
        cv2.imshow(window_title, image)

def main():
    window_title = 'Mouse Event'
    image = cv2.imread('../img/blank_500.jpg')
    cv2.imshow(window_title, image)
    cv2.setMouseCallback(window_title, draw_circle)
    
    while True:
        key = cv2.waitKey(0)
        if key == 27:  # ESC 키를 누르면 종료
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
