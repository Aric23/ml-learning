import sympy as sp
import numpy as np
import matplotlib.pyplot as plt 

x = sp.Symbol('x')
print(sp.diff(2*x**3 - 5*x**2 + 3*x - 7, x))
print(sp.diff(2.71828**(3*x), x))
print(sp.diff(sp.log(2*x + 1), x))

x, y = sp.symbols('x y')
f = 2*x**2*y + 3*x*y**2
df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)
print(df_dx)
print(df_dy)


def f1(x):
    return (x - 5)**2 + 1

def f1_grad(x):
    return 2*(x-5)

xs = []
xs_grad = []
learning_rate = 0.1
x = 8

for _ in range(30):
    xs.append(x)
    grad = f1_grad(x)
    xs_grad.append(grad)
    x = x - learning_rate * grad
    
    if abs(grad) < 0.001:
        break

print(f"икс в начале {xs[0]}, икс в конце {xs[-1]}")


learning_rates = [0.01 , 0.05, 0.1, 0.5]
iters = []
for lr in learning_rates:
    x = 8
    itr = 0
    for _ in range(30):
        
        
        xs = []
        xs_grad = []
        xs.append(x)
        grad = f1_grad(x)
        xs_grad.append(grad)
        x = x - lr * grad
        itr = itr + 1
    
        if abs(grad) < 0.001:
             break
    iters.append(itr)

for lr, iters in zip(learning_rates, iters):
    print(f"{lr} - {iters}")
    



    

