import numpy as np

X = np.array([[1, 1],        
     [2, 1],
     [3, 1],
     [4, 1]])
w_vec = np.array([0, 0, 0, 0])

 
def train(X, target, w_vec, lr, steps):
    n = len(target)
    for i in range(steps):
        y      = X @ w_vec
        err    = y - target
        loss   = np.mean(err ** 2)    
        grad = 2 * (X.T @ err) / n
        print(f"{i:3d}: w_vec={w_vec}  loss={loss:.6f}")   
        w_vec =  w_vec - lr * grad

    return w_vec


np.random.seed(0)
X_raw = np.random.rand(100, 3)
true_w = np.array([2.0, -3.0, 0.5])
b = np.ones((100, 1))
target = X_raw @ true_w  + 1 
X_raw = np.hstack((b ,X_raw))



X = np.array([[1,1],[2,1],[3,1],[4,1]], dtype=float)
H = 2 * (X.T @ X) / 4
print(H)
print(np.linalg.eigvalsh(H))