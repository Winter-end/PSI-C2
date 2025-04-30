import matplotlib.pyplot as plt

def plot_points(points1, points2, label1: str, label2: str):
    plt.scatter(points1, [0]*len(points1), color='blue', label=label1)
    plt.scatter(points2, [1]*len(points2), color='red', label=label2)
    plt.yticks([0, 1], [label1, label2])
    plt.xlim(min(min(points1), min(points2))-1, max(max(points1), max(points2))+1)
    plt.legend()
    plt.show()