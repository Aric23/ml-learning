import numpy as np
import matplotlib.pyplot as plt

a = [2, 3, 4]
b = [1, 0, 2]

a_np = np.array(a)
b_np = np.array(b)

def zad1(v1, v2):
    print(v1 + v2)
    print(v1 - v2)
    print(3 * v1)
    print(np.dot(v1, v2))
    print(np.linalg.norm(v1))
    print(np.linalg.norm(v2))

zad1(a_np, b_np)

v = [2, -1]
w = [1, 2]

v_np = np.array(v)
w_np = np.array(w)

def zad2(v1, v2):
    a = np.dot(v1, v2)
    
   
    if a == 0:
        print('ravno')
    else:
        print('net')

zad2(v, w)

v1 = [1, 0, 0]
v2 = [0, 1, 0]
v3 = [1, 1, 0]

v1_np = np.array(v)
v2_np = np.array(w)
v3_np = np.array(v)


def zad3(v1, v2, v3):
    a = np.dot(v1, v2)
    b = np.dot(v1, v3)
    c = np.dot(v2, v3)
    a1 = np.linalg.norm(v1)
    b1 = np.linalg.norm(v2)
    c1 = np.linalg.norm(v3)
    print(a / (a1 * b1))
    print(b / (a1 * c1))
    print(c / (b1 * c1))

zad3(v1_np, v2_np, v3_np)