import matplotlib.pyplot as plt

def plot_points(points1, points2, points3, label1: str, label2: str, label3: str):
    plt.scatter(points1, [0]*len(points1), color='blue', label=label1)
    plt.scatter(points2, [1]*len(points2), color='red', label=label2)
    plt.scatter(points3, [2]*len(points3), color='green', label=label3)
    plt.yticks([0, 1, 2], [label1, label2, label3])
    plt.xlim(min(min(points1), min(points2), min(points3))-1, max(max(points1), max(points2), max(points3))+1)
    plt.title('Wartości dla funkcji przystosowania bez skalowania i ze skalowaniem')
    plt.legend()
    plt.show()