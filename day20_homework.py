import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
# Загружаем датасет
diabetes = load_diabetes()
X = diabetes.data
y_continuous = diabetes.target
median_value = np.median(y_continuous)
y = (y_continuous > median_value).astype(int)

# Разбиваем на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Обучаем случайный лес (100 деревьев)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Делаем предсказания и считаем accuracy
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"Медиана целевой переменной: {median_value:.4f}")
print(f"Accuracy случайного леса: {acc:.4f}")

model1 = DecisionTreeClassifier(random_state=42, max_depth=3)
model1.fit(X_train, y_train)
print(f"acc леса  - {acc} и acc дерева - {accuracy_score(y_test, model1.predict(X_test))}")

importanse = model.importance = model.feature_importances_
print("\nВажность признаков:")
for i, imp in enumerate(importanse):
    print(f"Признак {i} - {imp}")


n_estimators = [10, 50, 100, 200, 500]
for e in n_estimators:
    model = RandomForestClassifier(n_estimators=e, random_state=42)
    model.fit(X_train, y_train)


    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"Accuracy случайного леса: {acc:.4f}")
