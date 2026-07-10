import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris
import seaborn as sns
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression

titanic = sns.load_dataset('titanic')

features = ['pclass', 'sex', 'age', 'fare']
titanic_clean = titanic[features + ['survived']].dropna()

titanic_clean['sex'] = titanic_clean['sex'].map({'male': 0, 'female':1})

X = titanic_clean[features]
y = titanic_clean['survived']

model = RandomForestClassifier(n_estimators=100 , random_state=42)
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"Mean - {scores.mean()} and std - {scores.std()}")

single_scores = []
for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
    model.fit(X_train, y_train)
    single_scores.append(accuracy_score(y_test, model.predict(X_test)))
    print(f"  run {i+1}: {single_scores[-1]:.3f}")

print(f"\nСредняя: {np.mean(single_scores):.3f} ± {np.std(single_scores):.3f}")
print(f"Разброс: {np.min(single_scores):.3f} - {np.max(single_scores):.3f}")

means = []

models = {
 'LogisticRegression' : LogisticRegression(random_state = 42, max_iter=1000),
 'DecisionTree' : DecisionTreeClassifier(random_state=42),
 'RandomForest' : RandomForestClassifier(n_estimators = 100, random_state=42)
}
result = {}
for name, model in models.items():
    scores= cross_val_score(model, X, y, cv=5, scoring='accuracy')
    result[name]={'mean' : scores.mean()}


for mean, (name, models) in zip(means, models.items()):
    print(f"{name} - {mean}")


print(f"best model - {max(result, key=lambda x: result[x]['mean'])}")

cvs = [3, 5, 10]

for cv in cvs:
    model1 = RandomForestClassifier(random_state=42, n_estimators=100)
    scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')
    print(f"Mean - {scores.mean()} and std - {scores.std()}")

print("\n" + "=" * 60)
print("СРАВНЕНИЕ МОДЕЛЕЙ ЧЕРЕЗ КРОСС-ВАЛИДАЦИЮ")
print("=" * 60)

# Загружаем данные (используем диабет для разнообразия)
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
X = diabetes.data
y = (diabetes.target > np.median(diabetes.target)).astype(int)

print(f"Размер: {X.shape}")
print(f"Класс 0: {sum(y==0)}, Класс 1: {sum(y==1)}")

# Создаём модели
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
}

# Оцениваем каждую модель с помощью кросс-валидации
results = {}
for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    results[name] = {
        'mean': scores.mean(),
        'std': scores.std(),
        'scores': scores
    }
    print(f"\n{name}:")
    print(f"  Средняя точность: {scores.mean():.3f} ± {scores.std():.3f}")
    print(f"  Фолды: {scores}")

# Визуализация
plt.figure(figsize=(10, 6))
positions = range(len(models))
means = [results[name]['mean'] for name in models]
stds = [results[name]['std'] for name in models]

plt.bar(positions, means, yerr=stds, capsize=10, color=['skyblue', 'lightgreen', 'salmon'])
plt.xticks(positions, models.keys(), rotation=15)
plt.ylabel('Точность (accuracy)')
plt.title('Сравнение моделей с помощью кросс-валидации (5 фолдов)')
plt.grid(axis='y', alpha=0.3)
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig('model_comparison.png', dpi=150)
plt.show()

# Вывод лучшей модели
best_model = max(results, key=lambda x: results[x]['mean'])
print(f"\n🏆 Лучшая модель: {best_model} (средняя точность = {results[best_model]['mean']:.3f})")