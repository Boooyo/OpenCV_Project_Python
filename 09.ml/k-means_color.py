import numpy as np
import cv2

def kmeans_color_quantization(image_path, K=16):
    # 이미지 읽기
    img = cv2.imread(image_path)
    
    # 이미지 데이터를 적절한 형식으로 변환하여 군집화에 사용
    data = img.reshape((-1, 3)).astype(np.float32)
    
    # 중심 이동 기준 설정
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    
    # K-Means 클러스터링 적용
    _, labels, centers = cv2.kmeans(data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    # 중심 값을 정수형으로 변환
    centers = np.uint8(centers)
    
    # 각 픽셀에 대한 군집 중심값 적용
    quantized = centers[labels.flatten()]
    
    # 원본 이미지 형태로 변환
    quantized = quantized.reshape(img.shape)
    
    # 원본 이미지와 군집화된 이미지를 수평으로 결합하여 출력
    merged = np.hstack((img, quantized))
    
    # 결과 출력
    cv2.imshow('KMeans Color Quantization', merged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 함수 호출하여 이미지에 대한 색상 양자화 수행
kmeans_color_quantization('../img/taekwonv1.jpg', K=16)
