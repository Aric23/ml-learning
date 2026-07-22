import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

print("=" * 60)
print("ВИЗУАЛИЗАЦИЯ ГРАДИЕНТНОГО СПУСКА")
print("=" * 60)

def f(x):
    return (x-3)**2 + 2

def grad_f(x):
    return 2 * (x-3)

def gradient_descent(start_x, learning_rate, n_steps):
    x = start_x
    path = [x]
    f_values = [f(x)]

    for _ in range(n_steps):
        grad = grad_f(x)
        x = x - learning_rate * grad
        path.append(x)
        f_values.append(f(x))

        if abs(grad) < 0.001:
            break

    return path, f_values

start_x = -5
learning_rate = 0.2
n_steps = 30

path, f_values = gradient_descent(start_x, learning_rate, n_steps)

x_vals = np.linspace(-6, 10, 200)
y_vals = f(x_vals)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x) = (x-3)² + 2')
plt.plot(path, f_values, 'ro-', linewidth=1, markersize=6, label='Путь спуска')
plt.scatter(path[0], f_values[0], color='green', s=100, label='Cтарт')
plt.scatter(path[-1], f_values[-1], color='red', s=100, label='Финиш')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Градиентовый спуск')
plt.grid(True, alpha=0.3)
plt.legend()

plt.subplot(1 , 2, 2)
plt.plot(range(len(f_values)), f_values, 'go-', linewidth=2)
plt.xlabel('Итерация')
plt.ylabel('f(x)')
plt.title('Уменьшение ошибки')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('gradient_descent_visual.png', dpi=150)
plt.show()

print(f"Начало: x = {start_x}, f(x) = {f(start_x):.4f}")
print(f"Конец: x = {path[-1]:.4f}, f(x) = {f_values[-1]:.4f}")
print(f"Итераций: {len(path)-1}")
print(f"Истинный минимум: x = 3, f(x) = 2")

print("\nСравнение learning_rate:")

learning_rates = [0.01, 0.1, 0.2, 0.8]
plt.figure(figsize=(12, 6))

for i, lr in enumerate(learning_rates, 1):
    path_lr, values_lr = gradient_descent(-5, lr, 30)
    
    plt.subplot(2, 2, i)
    plt.plot(x_vals, y_vals, 'b-', linewidth=2)
    plt.plot(path_lr, values_lr, 'ro-', linewidth=1, markersize=4)
    plt.scatter(path_lr[0], values_lr[0], color='green', s=50)
    plt.scatter(path_lr[-1], values_lr[-1], color='red', s=50)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'learning_rate = {lr}')
    plt.xlim(-6, 10)
    plt.ylim(0, 70)
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('learning_rate_comparison.png', dpi=150)
plt.show()