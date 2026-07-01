import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree

print("="*50)
print("ПРАКТИКА: Деревья решений")
print("="*50)

np.random.seed(42)

n=150

X0 = np.random.randn(n, 2) +  [1, 1] + 0.5
X1 = np.random.randn(n, 2) +  [3,3] + 0.5

y0 = np.ones(150)
y1 = np.zeros(150)

X = np.vstack([X0, X1])
y = np.hstack([y0, y1])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = DecisionTreeClassifier(random_state=42, max_depth=5)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

depths = [1,2,3,4,5,6,7,8,9,10]
accuracys = []

for depth in depths:
    np.random.seed(42)

    n=150

    X0 = np.random.randn(n, 2) +  [1, 1] + 0.5
    X1 = np.random.randn(n, 2) +  [3,3] + 0.5

    y0 = np.ones(150)
    y1 = np.zeros(150)

    X = np.vstack([X0, X1])
    y = np.hstack([y0, y1])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = DecisionTreeClassifier(random_state=42, max_depth=depth)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(accuracy)
    accuracys.append(accuracy)

print(f" Максимальное {max(accuracys)}")


plt.figure(figsize=(20, 10))
plot_tree(model, feature_names=['X1', 'X2'],
class_names=['Красный', 'Синий'],
filled=True,
rounded=True,
fontsize=10)
plt.title('Дерево решений (ограничения глубины)')
plt.show()