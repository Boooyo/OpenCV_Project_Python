import cv2
import numpy as np

# 카테고리 및 파일 경로 정의
categories = ['비행기', '오토바이']
dict_file = './plane_bike_dict.npy'
svm_model_file = './plane_bike_svm.xml'
imgs = ['../img/aircraft.jpg', '../img/jetstar.jpg', '../img/motorcycle.jpg', '../img/motorbike.jpg']

# SIFT 특징 추출기 생성
detector = cv2.xfeatures2d.SIFT_create()

# BOW 추출기 생성 및 어휘 로드
bow_extractor = cv2.BOWImgDescriptorExtractor(detector, cv2.BFMatcher(cv2.NORM_L2))
bow_extractor.setVocabulary(np.load(dict_file))

# 훈련된 SVM 모델 로드
svm_model = cv2.ml.SVM_load(svm_model_file)

# 이미지 테스트
for path in imgs:
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 테스트 이미지에서 BOW 히스토그램 추출
    hist = bow_extractor.compute(gray, detector.detect(gray))

    # SVM을 사용하여 예측
    _, result = svm_model.predict(hist)

    # 결과 표시
    predicted_class = categories[int(result[0][0])]
    text, _ = cv2.getTextSize(predicted_class, cv2.FONT_HERSHEY_PLAIN, 2, 3)
    x, y = 10, 50
    cv2.rectangle(img, (x, y - text[1]), (x + text[0], y + text[1]), (30, 30, 30), -1)
    cv2.putText(img, predicted_class, (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow(path, img)

cv2.waitKey(0)
cv2.destroyAllWindows()
