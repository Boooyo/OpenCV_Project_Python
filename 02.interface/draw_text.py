import cv2

def draw_texts(img, texts):
    for text in texts:
        cv2.putText(img, text[0], text[1], text[2], text[3], text[4])

def main():
    img = cv2.imread('../img/blank_500.jpg')

    # 텍스트와 속성 배열로 정의
    texts = [
        ("Plain", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,0)),                  # sans-serif small
        ("Simplex", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0,0)),              # sans-serif normal
        ("Duplex", (50, 110), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0,0)),               # sans-serif bold
        ("Simplex", (200, 110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,250)),           # sans-serif normal X2
        ("Complex Small", (50, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0,0)), # serif small
        ("Complex", (50, 220), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0,0)),              # serif normal
        ("Triplex", (50, 260), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0,0)),              # serif bold
        ("Complex", (200, 260), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,255)),            # serif normal X2
        ("Script Simplex", (50, 330), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 0,0)),# hand-wringing sans-serif
        ("Script Complex", (50, 370), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0, 0,0)),# hand-wringing serif
        ("Plain Italic", (50, 430), cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC, 1, (0, 0,0)), # sans-serif + italic
        ("Complex Italic", (50, 470), cv2.FONT_HERSHEY_COMPLEX | cv2.FONT_ITALIC, 1, (0, 0,0)) # sarif + italic
    ]

    # 텍스트 그리기
    draw_texts(img, texts)

    cv2.imshow('draw text', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
