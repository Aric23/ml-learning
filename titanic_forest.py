import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

print("Случайный лес")

titanic = sns.load_dataset('titanic')

features = ['pclass', 'sex', 'age', 'fare']
titanic_clean = titanic[features + ['survived']].dropna()

titanic_clean['sex'] = titanic_clean['sex'].map({'male': 0, 'female':1})

X = titanic_clean[features]
y = titanic_clean['survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

forest = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
forest.fit(X_train, y_train)
y_pred = forest.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)}")
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred))

importance = forest.feature_importances_
print("\nВажность признаков:")
for name, imp in zip(features, importance):
    print(f"{name}: {imp}")

plt.figure(figsize=(8,5))
plt.barh(features, importance, color='skyblue')
plt.xlabel('Важность')
plt.title('Важность признаков в случайном лесу')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('titanic_forest_features.png', dpi=150)
plt.show()