import numpy as np 

matrix = np.random.randint(1, 101, size=(5,5))
print(matrix)
print(np.sum(matrix))
print(np.mean(matrix))
print(np.min(matrix))
print(np.max(matrix))

matrix1 = np.random.randint(1, high = 100,size=(3,3))
matrix2 = np.random.randint(1, high = 100,size=(3,3))
print(matrix1 + matrix2)
print(matrix1- matrix2)
print(matrix1 * matrix2)

matrix3 = np.random.rand(50)
gn = 0
gm = 0
gd = 0
for i in range(50):
    if matrix3[i] > 0.7:
        gn+=1
    elif matrix3[i] < 0.3:
        gm+=1
    else:
        gd+=1
print(gn, gm, gd)

matrix4 = np.arange(20)
matrix5 = matrix4.reshape(4,5)
print(matrix5)
matrix6 = matrix4.reshape(2, 10)
print(matrix6)

flattened = matrix6.flatten()
print("Обратно в вектор:", flattened)
