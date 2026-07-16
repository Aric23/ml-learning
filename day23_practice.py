import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("ПРАКТИКА: МАТРИЧНЫЕ ОПЕРАЦИИ")
print("=" * 60)

# ========== ЗАДАНИЕ 1: Создание матриц ==========
print("\n1. Создание матриц")

A = np.array([[1,2,3], [4,5,6]])
B = np.array([[7,8], [9,10], [11,12]])
Z = np.zeros((2,2))
O = np.ones((4,4))
print(A)
print(B)
print(Z)
print(O)
# ========== ЗАДАНИЕ 2: Сложение и умножение на число ==========
print("\n2. Сложение и умножение на число")


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A + B)
print(A - B)
print(3 * A)
print(2 * A + 3*B)
# ========== ЗАДАНИЕ 3: Умножение матриц ==========
print("\n3. Умножение матриц")

G = np.array([[1, 2, 3], [4, 5, 6]])
H = np.array([[7, 8], [9, 10], [11, 12]])


print(G @ H)
try:
    print(H @ G)
except ValueError as es:
    print(es)

print(G @ G.T)

# ========== ЗАДАНИЕ 4: Транспонирование ==========
print("\n4. Транспонирование")

print(G.T)
print(np.array_equal(G, G.T))

# ========== ЗАДАНИЕ 5: Умножение матрицы на вектор ==========
print("\n5. Умножение матрицы на вектор")

# Даны:
A = np.array([[1, 2], [3, 4], [5, 6]])
v = np.array([10, 20])

print(A@v)
# Вычислите A × v
# Какой размер у результата?