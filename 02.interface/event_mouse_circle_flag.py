import cv2

# 창 제목과 이미지 설정
title = '마우스 이벤트'
img = cv2.imread('../img/blank_500.jpg')
cv2.imshow(title, img)

# 사전에 정의된 색상
colors = {'검정': (0, 0, 0),
          '빨강': (0, 0, 255),
          '파랑': (255, 0, 0),
          '초록': (0, 255, 0)}

# 마우스 이벤트 콜백 함수
def onMouse(event, x, y, flags, param):
    print(event, x, y, flags)  # 이벤트, 좌표, 플래그 출력
    color = colors['검정']  # 기본적으로 검정색 사용

    # 마우스 왼쪽 버튼 클릭 이벤트
    if event == cv2.EVENT_LBUTTONDOWN:
        # Ctrl 키와 Shift 키가 동시에 눌린 경우
        if flags & cv2.EVENT_FLAG_CTRLKEY and flags & cv2.EVENT_FLAG_SHIFTKEY:
            color = colors['초록']
        elif flags & cv2.EVENT_FLAG_SHIFTKEY:  # Shift 키만 눌린 경우
            color = colors['파랑']
        elif flags & cv2.EVENT_FLAG_CTRLKEY:   # Ctrl 키만 눌린 경우
            color = colors['빨강']

        # 반지름이 30인 원을 해당 좌표에 그림
        cv2.circle(img, (x, y), 30, color, -1)
        cv2.imshow(title, img)  # 그린 이미지 다시 표시

# 마우스 콜백 함수를 GUI 윈도우에 등록
cv2.setMouseCallback(title, onMouse)

# 종료 키가 눌릴 때까지 대기
while True:
    if cv2.waitKey(0) & 0xFF == 27:  # ESC 키로 종료
        break

# 모든 창 닫기
cv2.destroyAllWindows()
