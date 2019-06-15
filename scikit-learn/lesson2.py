import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
print(__doc__)


plt.figure(figsize=(12, 12))
n_samples = 1500
random_state = 170

# Generate isotropic Gaussian blobs for clustering
X, y = make_blobs(n_samples=n_samples, random_state=random_state)
print(X)
print(X.shape)  # The generated samples
print(y)  # The integer labels for cluster membership of each sample
y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)

print(y_pred)

plt.subplot(221)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title('incorrect number of blobs')


plt.show()
