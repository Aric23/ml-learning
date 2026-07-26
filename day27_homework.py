import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs, make_circles, make_moons

n_samples = 300
n_features = 2
n_clusters = 5
random_state = 42 

X, y_true = make_blobs(
    n_samples=n_samples,
    n_features=n_features,
    centers=n_clusters,
    cluster_std=0.8,
    random_state=random_state
)

kmens = KMeans(n_clusters=n_clusters, random_state=random_state, n_init = 10 )
y_pred = kmens.fit_predict(X)
plt.figure(figsize=(10,10))
colors = ['blue', 'red', 'green', 'orange', 'yellow']
for i in y_pred:
    mask = y_pred == i 
    plt.scatter(X[mask, 0], X[mask, 1], color=colors[i], alpha=0.6)

plt.grid(True, alpha=0.3)


Kms = range(1, 11)
inertia_list = []

for k in Kms:
    s  = KMeans(n_clusters = k, random_state=42, n_init = 10)
    s.fit(X)
    inertia_list.append(s.inertia_)

plt.figure(figsize=(10,10))
plt.plot(Kms, inertia_list, 'bo-', linewidth=2, markersize=6)


X, y_true = make_moons(
    n_samples=n_samples,
    random_state=random_state
)

