import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_diabetes
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

print("=" * 60)
print("ПРАКТИКА: Кросс-валидация")
print("=" * 60)

iris = load_iris()
X = iris.data
y = iris.target

model1 = LogisticRegression(random_state=42, max_iter=1000)
scores = cross_val_score(model1, X, y, cv=5, scoring='accuracy')
print(f"Mean - {scores.mean()} and std - {scores.std()}")

means = []

models = {
 'LogisticRegression' : LogisticRegression(random_state = 42, max_iter=1000),
 'DecisionTree' : DecisionTreeClassifier(random_state=42),
 'RandomForest' : RandomForestClassifier(n_estimators = 100, random_state=42)
}

for name, model in models.items():
    scores= cross_val_score(model, X, y, cv=5, scoring='accuracy')
    mean1 = scores.mean()
    means.append(mean1)


for mean, (name, models) in zip(means, models.items()):
    print(f"{name} - {mean}")

cvs = [3, 5, 10]

for cv in cvs:
    model1 = RandomForestClassifier(random_state=42, n_estimators=100)
    scores = cross_val_score(model1, X, y, cv=cv, scoring='accuracy')
    print(f"Mean - {scores.mean()} and std - {scores.std()}")

print("=" * 60)
print("ПРАКТИКА: 'accuracy', 'precision_macro', 'recall_macro'")
print("=" * 60)

scorings = ['accuracy', 'precision_macro', 'recall_macro' ]

for score in scorings:
    model1 = RandomForestClassifier(random_state=42, n_estimators=100)
    scores = cross_val_score(model1, X, y, cv=5, scoring=score)
    print(scores)
