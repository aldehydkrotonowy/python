import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
from sklearn import datasets

iris = datasets.load_iris()
digits = datasets.load_digits()

print(iris)
print('----------')
print(digits)
print('----------')
np.random.seed(10)
data, labels = datasets.make_moons(n_samples=200, noise=0.09, random_state=0)
print(data.shape, labels.shape)
color_map = matplotlib.colors.LinearSegmentedColormap.from_list("", [
                                                                "red", "yellow"])
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap=color_map)
plt.show()
