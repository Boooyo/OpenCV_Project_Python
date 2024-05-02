import numpy as np
import cv2
import matplotlib.pyplot as plt

def generate_random_data(low, high, size):
    return np.random.randint(low, high, size)

def plot_clusters(data, label, center):
    colors = ['r', 'b']
    markers = ['s', 'o'] # 정사각형과 원 표시
    for i in range(len(colors)):
        cluster_data = data[label.ravel() == i]
        plt.scatter(cluster_data[:, 0], cluster_data[:, 1], c=colors[i])
        plt.scatter(center[i, 0], center[i, 1], s=100, c=colors[i], marker=markers[i])
    plt.show()

def main():
    # 랜덤 데이터 생성
    a = generate_random_data(0, 150, (25, 2))
    b = generate_random_data(128, 255, (25, 2))
    data = np.vstack((a, b)).astype(np.float32)

    # 중지 조건 정의
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    # k-means 클러스터링 적용
    ret, label, center = cv2.kmeans(data, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # 클러스터링 결과 플롯
    plot_clusters(data, label, center)

if __name__ == "__main__":
    main()
