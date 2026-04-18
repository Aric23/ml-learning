import numpy as np 
import matplotlib.pyplot as plt

print("Ленейная регрессия с помощью нум пу")

np.random.seed(42)
X = np.random.rand(100, 1) * 10
true_slope = 2.5
true_intercept = 1.0
y = true_slope * X + true_intercept + np.random.randn(100, 1) * 2
print(f"Сгененрировано {len(X)} точек")
print(f"Истинная зависимость: y = {true_slope:.1f} * x + {true_intercept:.1f}")

X_b = np.c_[np.ones((100, 1)), X]  # добавляем единицы слева

# Нормальное уравнение: θ = (X^T * X)^(-1) * X^T * y
theta_best = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y

intercept = theta_best[0, 0]
slope = theta_best[1, 0]

print(f"\nНайденная зависимость: y = {slope:.3f} * x + {intercept:.3f}")

# ========== 3. Предсказания ==========
X_new = np.array([[0], [10]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b @ theta_best

print(f"\nПредсказания:")
print(f"  При x = 0: y = {y_predict[0, 0]:.2f}")
print(f"  При x = 10: y = {y_predict[1, 0]:.2f}")

# ========== 4. Оценка качества ==========
y_pred = X_b @ theta_best
mse = np.mean((y - y_pred) ** 2)
rmse = np.sqrt(mse)
r2 = 1 - (np.sum((y - y_pred) ** 2) / np.sum((y - np.mean(y)) ** 2))

print(f"\n📊 Метрики качества:")
print(f"  MSE: {mse:.3f}")
print(f"  RMSE: {rmse:.3f}")
print(f"  R²: {r2:.3f}")

# ========== 5. Визуализация (если установлен matplotlib) ==========
try:
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, alpha=0.7, label="Исходные данные")
    plt.plot(X_new, y_predict, 'r-', linewidth=2, label="Линия регрессии")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.title("Линейная регрессия")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
except:
    print("\n(Для визуализации установите matplotlib: pip install matplotlib)")

# ========== 6. Предсказание для нового значения ==========
while True:
    try:
        x_input = float(input("\nВведите x для предсказания (или 'exit'): "))
        x_pred = np.array([[1, x_input]])  # 1 для intercept, x_input
        y_pred = x_pred @ theta_best
        print(f"Предсказанное y: {y_pred[0, 0]:.2f}")
    except ValueError:
        print("До свидания!")
        break
    except:
        print("Ошибка! Введите число.")