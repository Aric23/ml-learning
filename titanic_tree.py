import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import plot_tree

print("🚢 Дерево решений для Titanic")

titanic = sns.load_dataset('titanic')

features = ['pclass', 'sex', 'age', 'fare']
titanic_clean = titanic[features + ['survived']].dropna()

titanic_clean['sex'] = titanic_clean['sex'].map({'male': 0, 'female' : 1})

X = titanic_clean[features]
y = titanic_clean['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42)

model = DecisionTreeClassifier(max_depth= 4, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred))

plt.figure(figsize=(15, 10))
plot_tree(model, feature_names = features,
class_names = ["Выжил","Погиб"],
filled = True,
rounded = True,
fontsize = 8)
plt.title("Дерево решений для Titanic (глубина 4)")
plt.tight_layout()
plt.savefig('titanic_tree.png', dpi=150)
plt.show()