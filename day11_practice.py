import numpy as np

vector = np.arange(10)
print("Vector:", vector)

matrix_ones = np.ones((3,3))
print("Matrix ones:", matrix_ones)

random_matrix = np.random.rand(2,5)
print("Random matrix:", random_matrix)

identity = np.eye(4)
print("id: ", identity)

full_matrix = np.full((3,4), 7)
print("full matrix: ", full_matrix)

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print(a+b)
print(a * 5)
print(a **2)
print(np.mean(b))
print(np.max(a))
print(np.sum(a))

arr = np.arange(1, 13)  # [1 2 3 4 5 6 7 8 9 10 11 12]
print("Исходный массив:", arr)
print("Размерность:", arr.shape)

matrix = arr.reshape(3,4)
print(matrix)
matrix2 = arr.reshape(2, 6)
print(matrix2)

flattened = matrix.flatten()
print("Обратно в вектор:", flattened)

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

print("Исходная матрица:\n", matrix)
print("Третий столбец:", matrix[:, 2])
print("Подматрица:\n", matrix[0:2, 2:4])
print("Всё после [1,1]:\n", matrix[1:, 1:])
matrix[1, 1] = 99
print("Изменённая матрица:\n", matrix)