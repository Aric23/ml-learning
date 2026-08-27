import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("ПРАКТИКА: ГРАДИЕНТНЫЙ СПУСК ДЛЯ ЛИНЕЙНОЙ РЕГРЕССИИ")
print("=" * 60)

# ========== ЗАДАНИЕ 1: Линейная регрессия с GD ==========
print("\n1. Линейная регрессия с GD")
np.random.seed(42)
X = np.random.randn(100, 1) * 10
y = 3 * X + 2 + np.random.randn(100, 1)

X= X.flatten()
y = y.flatten()
def grad(b,w, X, y):
    n = len(X)
    y_pred = w * X + b
    grad_b = (2/n) * np.sum(y_pred- y)
    grad_w  =(2/n) * np.sum((y_pred - y) *X)
    return grad_b, grad_w
def loss_function(X, y, w, b):
    y_pred = X*w + b 
    return np.mean((y - y_pred)**2)

def grdientspuskbla(X, y, w_init, b_init, learning_rate, iters):
    w = w_init
    b = b_init
    b_history = [b]
    w_history = [w]
    loss_history = [loss_function(X, y, w, b)]

    for i in range(iters):
        grad_b, grad_w = grad(b, w, X, y)
        b = b - learning_rate * grad_b
        w = w - learning_rate * grad_w
        loss_history.append(loss_function(X, y, w, b))
        b_history.append(b)
        w_history.append(w)
        if abs(grad_b ) < 0.0001 and abs(grad_w) < 0.0001:
            break

    return b_history, w_history, loss_history

b_history, w_history, loss_history = grdientspuskbla(X, y, w_init =0.0, b_init=0.0, learning_rate=0.01, iters=99)

plt.figure(figsize=(10, 10))
plt.plot(range(len(loss_history)), loss_history, 'r-', label = 'X*w + b')
plt.ylabel('MSE')
plt.xlabel('Итерация')
plt.title('График сходимости')
plt.legend()
plt.grid(True, alpha=0.4)
plt.show()

# ========== ЗАДАНИЕ 2: Сравнение с sklearn ==========
print("\n2. Сравнение с sklearn")
from sklearn.linear_model import LinearRegression
final_w = w_history[-1]
final_b = b_history[-1]
model = LinearRegression()
model.fit(X.reshape(-1, 1), y)
print(f"\nСравнение с sklearn:")
print(f"  sklearn: w = {model.coef_[0]:.4f}, b = {model.intercept_:.4f}")
print(f"  GD:      w = {final_w:.4f}, b = {final_b:.4f}")

# ========== ЗАДАНИЕ 3: Разные начальные точки ==========
print("\n3. Разные начальные точки")
X1 = np.random.randn(100, 1) * 10 + (0, 0)
X2 = np.random.randn(100, 1) * 10 + (5, 5)
X3 = np.random.randn(100, 1) * 10 + (-5, 10)
Xr = [X1, X2, X3]


# Попробуйте начальные точки: (0, 0), (5, 5), (-5, 10)
# Как это влияет на сходимость?

# ========== ЗАДАНИЕ 4: Визуализация траектории ==========
print("\n4. Визуализация траектории")
X = np.random.randn(100, 1) * 10
y = 3 * X + 2 + np.random.randn(100, 1)
X, Y = np.meshgrid(X, y)
Z = (1/len(X))
print(Z.shape)
plt.figure(figsize=(10,10))
new_lost = loss_history
newlost = np.array(loss_history).reshape(-1,1)
plt.contour(X, Y, Z, 'b-', level = 20)
plt.plot(range(len(loss_history)), loss_history, 'r-', label = 'X*w + b')
# Нарисуйте contour plot функции потерь
plt.show()
# Отметьте на нём траекторию градиентного спуска

