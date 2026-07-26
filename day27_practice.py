import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_moons, make_circles

print("=" * 60)
print("ПРАКТИКА: KMEANS КЛАСТЕРИЗАЦИЯ")
print("=" * 60)

# ========== ЗАДАНИЕ 1: KMeans на разных данных ==========
print("\n1. KMeans на разных данных")


n_samples = 300
n_features = 2

random_state = 42

X, y_true = make_moons(
    n_samples=n_samples,
    random_state=random_state
)

kmens = KMeans(n_clusters=2, random_state=42, n_init=10)
y_pred = kmens.fit_predict(X)
centers = kmens.cluster_centers_

plt.figure(figsize=(15,15))
plt.grid(True, alpha=0.3)
colors = ['blue', 'red']
for i in y_pred:
    mask = y_pred == i 
    plt.scatter(X[mask, 0], X[mask, 1], color = colors[i], alpha=0.6, label=f'Кластер {i}')

plt.xlabel('first target')
plt.ylabel('second target')
plt.scatter(centers[:, 0], centers[:, 1], color='black',  marker='x', s=200, label='Center of claster')
plt.legend()
plt.show()
# ========== ЗАДАНИЕ 2: Метод локтя ==========
print("\n2. Метод локтя")

kms = range(1, 11)
inertia_list = []

for k in kms:
    kmens = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmens.fit(X)
    inertia_list.append(kmens.inertia_)


plt.figure(figsize=(10,10))
plt.plot(kms, inertia_list, 'bo-', linewidth=2,  markersize=8, alpha = 0.6)
plt.show()
# Для данных из задания 1 постройте график inertia для K от 1 до 10
# Где находится "локоть"?

# ========== ЗАДАНИЕ 3: Масштабирование данных ==========
print("\n3. Масштабирование данных")


x = np.random.randn(100, 1) * 10
y = np.random.randn(100, 1) * 1000
X = np.hstack([x, y])
kmens = KMeans(n_clusters = 4, random_state = 42, n_init = 10)
y_pred = kmens.fit_predict(X)
plt.figure(figsize=(10,10))
colors = ['blue', 'red', 'green', 'orange']
for i in range(4):
    mask = y_pred == i
    plt.scatter(X[mask, 0], X[mask, 1], color = colors[i], linewidth =2, label = f"Кластер {i}")

plt.grid(True, alpha=0.3)
plt.show()
# Создайте данные с сильно разными масштабами признаков
# Обучите KMeans без масштабирования и с масштабированием
# Сравните результаты

# ========== ЗАДАНИЕ 4: Собственный эксперимент ==========
print("\n4. Собственный эксперимент")

# Создайте свой набор данных (например, из 3-5 кластеров)
# Попробуйте разные K и выберите лучший