import numpy as np

print("=" * 60)
print("ПРАКТИКА: ОПРЕДЕЛИТЕЛИ, ОБРАТНЫЕ МАТРИЦЫ, СИСТЕМЫ")
print("=" * 60)

# ========== ЗАДАНИЕ 1: Определитель ==========
print("\n1. Определитель матрицы")

# Найдите определитель матриц:
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 3], [4, 6]])
C = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])

A_det = np.linalg.det(A)
B_det = np.linalg.det(B)
C_det = np.linalg.det(C)
print(f"A - {A_det}")
print(f"B - {B_det}")
print(f"AC - {C_det}")
res = {
 "A_det": A_det,
 "B_det": B_det,
 "C_det": C_det,
}
for det in res:
    if res[det] == 0:
        print(f"Оприделитель равен 0 у {det}")
    
# ========== ЗАДАНИЕ 2: Обратная матрица ==========
print("\n2. Обратная матрица")

A_inv = np.linalg.inv(A)
G = A @ A_inv
print(np.allclose(G, np.eye(2)))

# ========== ЗАДАНИЕ 3: Решение системы уравнений ==========
print("\n3. Решение системы уравнений")

# Решите систему:
# 3x + y = 9
# x + 2y = 8

a = np.array([[3, 1],[1, 2]])
b = np.array([9, 8])

resh = np.linalg.solve(a, b)
print(f"x - {resh[0]}, y - {resh[1]}")


# ========== ЗАДАНИЕ 4: Система 3×3 ==========
print("\n4. Система 3×3")

# Решите систему:
# x + 2y + z = 4
# 2x + y + z = 5
# x + y + 2z = 5

a = np.array([[1, 2, 1],[2, 1, 1],[1, 1, 2]])
b = np.array([4, 5, 5])

resh1 = np.linalg.solve(a,b)
print(f"x - {resh1[0]}, y - {resh1[1]}, z - {resh1[2]}")

# ========== ЗАДАНИЕ 5: Нормальное уравнение ==========
print("\n5. Нормальное уравнение")

# Создайте простые данные: X = [[1], [2], [3]], y = [2, 4, 6]
# Добавьте столбец единиц
# Найдите коэффициенты линейной регрессии через нормальное уравнение

np.random.seed(42)
X = np.random.randn(100, 1) * 10
y = 2.5 * X + 1 + np.random.randn(100, 1) * 2 

X_l = np.c_[np.ones((100,1)), X]

brush = np.linalg.inv(X_l.T @ X_l) @ X_l.T @ y

print(f"  intercept (b): {brush[0]:.3f}")
print(f"  slope (w): {brush[1]:.3f}")