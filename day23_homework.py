import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[1, 2, 3], [4, 5, 6]])

print(A + B)
print(2 * A)
print(A @ B)
print(A @ C)
print(C @ C.T)

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.T)
print((A.T).T)
print(np.array_equal(A, (A.T).T))


A = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([10, 20, 30])

print(A @ v)

A = np.array([[1, 2, 3], [2, 3, 4], [3, 4,5]])
print(np.array_equal(A, A.T))
