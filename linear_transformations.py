import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("ЛИНЕЙНЫЕ ПРЕОБРАЗОВАНИЯ: Поворот и масштабирование")
print("=" * 60)

# ========== 1. СОЗДАЁМ ФИГУРУ (НАБОР ТОЧЕК) ==========

points = np.array([
    [0, 0],
    [1, 0],
    [0, 1],
    [0, 0]  # замыкаем треугольник
])

print("Исходная фигура (треугольник):")
print(points)

scale_matrix = np.array([[2, 0], [0, 2]])

angle = np.pi / 4
rotation_matrix = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle), np.cos(angle)]
])

# Матрица отражения по оси X
reflect_x = np.array([[1, 0], [0, -1]])

scaled_points = (scale_matrix @ points.T).T
rotated_points = (rotation_matrix @ points.T).T
reflected_points = (reflect_x @ points.T).T

# ========== 4. ВИЗУАЛИЗАЦИЯ ==========
plt.figure(figsize=(12, 10))

# Исходная фигура
plt.subplot(2, 2, 1)
plt.plot(points[:, 0], points[:, 1], 'bo-', linewidth=2)
plt.xlim(-2, 3)
plt.ylim(-2, 3)
plt.grid(True, alpha=0.3)
plt.title('Исходная фигура')
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)

# Масштабирование
plt.subplot(2, 2, 2)
plt.plot(scaled_points[:, 0], scaled_points[:, 1], 'ro-', linewidth=2)
plt.xlim(-2, 3)
plt.ylim(-2, 3)
plt.grid(True, alpha=0.3)
plt.title('Масштабирование (×2)')
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)

# Поворот
plt.subplot(2, 2, 3)
plt.plot(rotated_points[:, 0], rotated_points[:, 1], 'go-', linewidth=2)
plt.xlim(-2, 3)
plt.ylim(-2, 3)
plt.grid(True, alpha=0.3)
plt.title('Поворот на 45°')
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)

# Отражение
plt.subplot(2, 2, 4)
plt.plot(reflected_points[:, 0], reflected_points[:, 1], 'mo-', linewidth=2)
plt.xlim(-2, 3)
plt.ylim(-3, 2)
plt.grid(True, alpha=0.3)
plt.title('Отражение по оси X')
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)

plt.tight_layout()
plt.savefig('linear_transformations.png', dpi=150)
plt.show()

print("✅ Преобразования применены!")
print("\nМатрицы преобразований:")
print(f"Масштабирование (×2):\n{scale_matrix}")
print(f"\nПоворот (45°):\n{rotation_matrix}")
print(f"\nОтражение по X:\n{reflect_x}")