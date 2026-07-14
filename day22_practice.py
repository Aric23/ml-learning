import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("ПРАКТИКА: Векторные операции")
print("=" * 60)

# ========== ЗАДАНИЕ 1: Сложение и вычитание ==========
print("\n1. Сложение и вычитание")


a = [2, 4, 6]
b = [1, 3, 5]
result_sum = []
result_min = []

for i in range(len(a)):
    result_sum.append(a[i] + b[i])
    result_min.append(a[i] - b[i])

a_np = np.array(a)
b_np = np.array(b)
result_sum_np = a_np + b_np
result_min_np = a_np - b_np


# ========== ЗАДАНИЕ 2: Умножение на скаляр ==========
print("\n2. Умножение на скаляр")

v = [1, 2, 3]
f = [2, -1, 0.5]
np_f = np.array(f)
np_v = np.array(v)
print(f"{np.dot(np_v, np_f)}")
     
# Что происходит с направлением и длиной?

# ========== ЗАДАНИЕ 3: Скалярное произведение ==========
print("\n3. Скалярное произведение")


a = [1, 0]
b = [0, 1] 
a_np = np.array(a)
b_np = np.array(b)
print(f"{np.dot(a_np, b_np)}")
a = [1, 1]
b = [2, 2]  
a_np = np.array(a)
b_np = np.array(b)
print(f"{np.dot(a_np, b_np)}")
# Объясните результаты

# ========== ЗАДАНИЕ 4: Норма вектора ==========
print("\n4. Норма вектора")


v = [3, 4]
np_v = np.array(v) 
norm_np = np.linalg.norm(np_v)
print(norm_np)
v = [1, 1, 1] 
np_v = np.array(v) 
norm_np = np.linalg.norm(np_v)
print(norm_np)

# ========== ЗАДАНИЕ 5: Визуализация векторов ==========
print("\n5. Визуализация векторов")
plt.figure(figsize=(20,20))

v = [2, 3]
w = [4, 1]
np_v = np.array(v)
np_w = np.array(w)
res = np_v + np_w
plt.plot([0, res[0]], [0, res[1]], c='skyblue', marker='o', label='v+w')
plt.plot(np_v, c='green')
plt.plot(np_w, c='red')


plt.show()
# На том же графике покажите их сумму v + w
# Используйте matplotlib для рисования стрелок