import numpy as np 

A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 4], [1, 2]])

det_A = np.linalg.det(A)
print(det_A)
if det_A == 0:
    print("Оприделитель равен 0 матрица не обратима")
else:
    A_inv = np.linalg.inv(A)
    print(f"Обратная матрица {A_inv}")
    a = A @ A_inv
    print(f"A × A⁻¹ = E - {np.allclose(a, np.eye(2))}")

det_B = np.linalg.det(B)
if det_B == 0:
    print("Оприделитель равен 0 матрица не обратима")
else:
    B_inv = np.linalg.inv(B)
    print(f"Обратная матрица {B_inv}")
    b = B @ B_inv
    print(f"A × A⁻¹ = E - {np.all_close(b, np.eye(2))}")

#4x + y = 10
#3x + 2y = 12

A = np.array([[4, 1], [3, 2]])
b = np.array([10, 12])
res = np.linalg.solve(A, b)
print(f"Ответ - {res}")


#x + y + z = 3
#x - y + z = 1
#2x + y - z = 2

A3 = np.array([[1, 1, 1], [1, -1, 1], [2, 1, -1]])
b3 = np.array([3, 1, 2])
res3 = np.linalg.solve(A3, b3)
print(f"Ответ - {res3}")

#(1, 2), (2, 3), (3, 5), (4, 6)
A4 = np.array([[1,2],[2,3],[3,5],[4,6]])
n1 = A4.shape[0]
n2 = A4.shape[1]
y4 = 2.5 * A4 + np.random.randn(n1, n2)

bach = np.linalg.inv(A4.T@A4) @ A4.T @ y4
print(f"1 - {bach[0]}, 2 - {bach[1]}")



    