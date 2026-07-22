import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

print("=" * 60)
print("ПРАКТИКА: ПРОИЗВОДНЫЕ И ГРАДИЕНТ")
print("=" * 60)

# ========== ЗАДАНИЕ 1: Производные вручную ==========
print("\n1. Производные вручную")

x = sp.Symbol('x')
print(sp.diff(4*x**3 + 2*x**2-3*x + 1, x))
print(sp.diff(2.71828**(2*x),x))
print(sp.diff(sp.log(3*x),x))
# Проверьте себя через SymPy

# ========== ЗАДАНИЕ 2: Частные производные ==========
print("\n2. Частные производные")
x, y = sp.symbols('x y')

f = 3*x**2*y + 2*x*y**2
print(sp.diff(f, x))
print(sp.diff(f, y))
grad = [sp.diff(f, x), sp.diff(f, y)]
print(grad)

# ========== ЗАДАНИЕ 3: Градиентный спуск ==========
print("\n3. Градиентный спуск")
def f1(x):
    return (x - 3)**2

def f1_grad(x):
    return  2*(x-3)

x = 0.0
learning_rate = 0.1
iteractions = 100
for i in range(iteractions):
    grad = f1_grad(x)
    x_new = x - learning_rate * grad
    x = x_new

    if abs(grad) < 0.001:
        break

print(grad)


# Реализуйте градиентный спуск для f(x) = (x - 3)²
# Начальная точка: x = 0
# learning_rate = 0.1
# Остановка: при |grad| < 0.001 или 100 итераций

# ========== ЗАДАНИЕ 4: Влияние learning_rate ==========
print("\n4. Влияние learning_rate")

learning_rate = [0.01, 0.1, 0,5, 0.9]

# Для f(x) = x² попробуйте разные learning_rate:
# 0.01, 0.1, 0.5, 0.9
# Что происходит с сходимостью?

# ========== ЗАДАНИЕ 5: Визуализация ==========
print("\n5. Визуализация")

x1 = np.linspace(-5, 5, 100)
def f4(x):
    return (x - 2)**2
y1 = f4(x1)
def grad_f4(x):
    return 2*(x-2)

x = 10.0
learning_rate = 0.1
path_x = [x]
path_y = [f1(x)]

for _ in range(20):
    grad = grad_f4(x)
    x = x - learning_rate * grad
    path_x.append(x)
    path_y.append(f4(x))
    if abs(grad) < 0.001:
        break

plt.figure(figsize=(10,10))
plt.plot(path_x, path_y, 'b-', linewidth=1, markersize=6, label='Градиентный спуск')
plt.plot(x1, y1, 'r-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('f(x) = (x - 2)²')
plt.show()
# Нарисуйте функцию f(x) = (x - 2)²
# Отметьте на ней траекторию градиентного спуска (20 шагов)