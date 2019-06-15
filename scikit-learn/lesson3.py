import numpy as np
import matplotlib.pyplot as plt

X = -2 * np.random.rand(100, 2)
X1 = 1 + 2 * np.random.rand(50, 2)
print(X, X1)
X[50:100, :] = X1
plt.scatter(X[:, 0], X[:, 1], s=50, c='b')
plt.show()
