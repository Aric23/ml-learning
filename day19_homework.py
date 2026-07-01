import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import plot_tree

iris = sns.load_dataset('iris')
print(iris.head())

iris_new = iris[['sepal_width', 'species', 'petal_length']].dropna()

X = iris_new[['sepal_width', 'petal_length']]
y = iris_new['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)

model = DecisionTreeClassifier(random_state = 42, max_depth=3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"accuracy - {accuracy_score(y_test, y_pred)}")

depths = [1,2,3,4,5,6,7,8,9,10]
depth_accuracy=[]
for depth in depths:
    iris = sns.load_dataset('iris')
    

    iris_new = iris[['sepal_width', 'species', 'petal_length']].dropna()

    X = iris_new[['sepal_width', 'petal_length']]
    y = iris_new['species']

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)

    model = DecisionTreeClassifier(random_state = 42, max_depth=depth)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    s = accuracy_score(y_test, y_pred)
    depth_accuracy.append(s)

plt.figure(figsize=(10,10))
plt.plot(depths, depth_accuracy)
plt.xlabel('depths')
plt.ylabel('depth_accuracy')
plt.show()

plt.figure(figsize=(10, 10))
plot_tree(model, feature_names=['Высота', 'Размер'], filled = True,
rounded = True,
fontsize = 8)
plt.title("Дерево решений для Titanic (глубина 4)")
plt.tight_layout()
plt.savefig('titanic_tree.png', dpi=150)
plt.show()

importance = model.feature_importances_

for name, imp in zip(X, importance):
    print(f"{name} -> {imp}")

max_index = importance.argmax()
most_important_feature = X[max_index]
print(f"max feature {most_important_feature}")