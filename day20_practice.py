import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris
import seaborn as sns

print("=" * 60)
print("ПРАКТИКА: Случайный лес")
print("=" * 60)
iris = sns.load_dataset('iris')

print(iris.head())

iris = iris.dropna()

y_iris = iris['species']
iris= iris.drop(columns='species') 


X_train, X_test, y_train, y_test = train_test_split(iris, y_iris, test_size=0.3)
model = RandomForestClassifier(random_state=42, max_depth=10)
model.fit(X_train, y_train)

print(f"acc - {accuracy_score(y_test, model.predict(X_test))}")
iris1 = sns.load_dataset('iris')
iris1 = iris1.dropna()

y_iris1 = iris1['species']
iris1= iris1.drop(columns='species') 


X_train1, X_test1, y_train1, y_test1 = train_test_split(iris, y_iris, test_size=0.3)


model1 = DecisionTreeClassifier(random_state=42, max_depth=3)
model1.fit(X_train1, y_train1)

print(f"Сравниваем acc одного дерева и леса")
print(f"acc Леса - {accuracy_score(y_test, model.predict(X_test))}")
print(f"acc Дерева - {accuracy_score(y_test1, model1.predict(X_test1))}")
print()