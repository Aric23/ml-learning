import numpy as np 
matrixs = np.ones((5,5))
matrixs1 = np.arange(1,6)
result = matrixs * matrixs1[:, np.newaxis]
print(result)

matrix2 = np.random.randint(1,10, size=(4,6))
print("Матрица -", matrix2)
print(np.mean(matrix2, axis=1))
print(np.max(matrix2, axis=0))
print(np.sum(matrix2))
print(np.std(matrix2, axis=1))

coeffs = np.array([[1, 1, 1], [2, 1,1],[1,1,2]])
results = np.array([6, 1,5])
solution = np.linalg.solve(coeffs, results)
print(f"Решение: x = {solution[0]}, y = {solution[1]} z = {solution[2]}")

A1 = np.random.rand(3,3) * 10
B1 = np.random.rand(3,3) * 10

print(A1+B1)
print(A1-B1)
print(A1 @ B1)
print(A1 * B1)