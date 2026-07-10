import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("🔬 Надёжная оценка модели")

diabetes = load_diabetes()
X = diabetes.data
y = (diabetes.target > np.median(diabetes.target)).astype(int)

model = RandomForestClassifier(n_estimators=100, random_state=42)

print("\n1. Одна случайная выборка (повтор 10 раз):")
single_scores = []
for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
    model.fit(X_train, y_train)
    single_scores.append(accuracy_score(y_test, model.predict(X_test)))
    print(f"  run {i+1}: {single_scores[-1]:.3f}")

print(f"\nСредняя: {np.mean(single_scores):.3f} ± {np.std(single_scores):.3f}")
print(f"Разброс: {np.min(single_scores):.3f} - {np.max(single_scores):.3f}")

print("\n2. Кросс-валидация (10 фолдов):")
cv_scores = cross_val_score(model, X, y, cv=10, scoring='accuracy')
print(f"  Фолды: {cv_scores}")
print(f"\nСредняя: {np.mean(cv_scores):.3f} ± {np.std(cv_scores):.3f}")
print(f"Разброс: {np.min(cv_scores):.3f} - {np.max(cv_scores):.3f}")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.boxplot([single_scores], label = ['train_test_split'])
plt.ylabel('Accuracy')
plt.title('Одна случайная выборка (10 раз)')
plt.ylim(0, 1)

plt.subplot(1, 2, 2)
plt.boxplot([cv_scores], label=['Кросс-валидация'])
plt.ylabel('Accuracy')
plt.title('Кросс-валидация (10 фолдов)')
plt.ylim(0, 1)

plt.tight_layout()
plt.savefig('evaluation_comparison.png', dpi=150)
plt.show()


