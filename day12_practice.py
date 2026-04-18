import numpy as np 

matrix = np.random.rand(3, 4)
print("Исходная матрица:", matrix)

row_vector = np.random.rand(4)
print("Вектор-строка:", row_vector)

result1 = matrix + row_vector
print("Матрица + веткор-строка: ", result1)

col_vector = np.random.rand(3, 1)
print("Вектор-столбец - :" ,col_vector)

result2 = matrix + col_vector
print("Матрица + вектор столбец: ", result2)

result3 =  matrix * 10
print("Матрица * 10: ", result3)

arr = np.arange(0, 10.5, 0.5)
print("Массив: ", arr)

print("Квадратный корень: ", np.sqrt(arr))

print("Экспонента: ", np.exp(arr))

print("Округление: ", np.floor(arr))

sin_values = np.sin(arr)
mask = sin_values > 0.5
print("Индексы sin > 0.5: ", np.where(mask))

matrix = np.random.randint(1, 21, size=(4,5))
print("Исходная матрица: ", matrix)

print("Общая сумма: ", np.sum(matrix))
print("Сумма по строкам: ",np.mean(matrix, axis=1))
print("Сумма по столбцам: ", np.sum(matrix, axis = 0))

A = np.array([[2,1], [1,3]])
B = np.array([[1,2], [3,4]])

print("Матрица A:\n", A)
print("Матрица B:\n", B)

print("A + B:\n", A + B)
print("A @ B:\n", A @ B)

A_inv = np.linalg.inv(A)
print("Обратная A:\n", A_inv)

# 5. Проверьте, что A @ A_inv = E
print("A @ A_inv:\n", A @ A_inv)

# 6. Решите систему:
# 2x + y = 5
# x + 3y = 10
coeffs = np.array([[2, 1], [1, 3]])
results = np.array([5, 10])
solution = np.linalg.solve(coeffs, results)
print(f"Решение: x = {solution[0]}, y = {solution[1]}")