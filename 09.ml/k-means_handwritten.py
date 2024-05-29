import cv2
import numpy as np
import matplotlib.pyplot as plt
import mnist

# MNIST 데이터 로드
data, _ = mnist.getData()

# k-means 클러스터링의 중지 조건 설정 (10회 반복 또는 1.0 이하의 정확도)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# k-means 클러스터링 적용, 10개의 클러스터로 분할
ret, labels, centers = cv2.kmeans(data, 10, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# 각 클러스터의 중심을 이미지로 변환하여 출력
plt.figure(figsize=(10, 5))
for i in range(10):
    # 각 클러스터 중심을 20x20 이미지로 변환
    center_img = centers[i].reshape(20, 20).astype(np.uint8)
    plt.subplot(2, 5, i + 1)
    plt.imshow(center_img, cmap='gray')
    plt.xticks([])
    plt.yticks([])

plt.show()
