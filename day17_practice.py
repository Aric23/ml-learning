import numpy as np
import seaborn as sns  
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


print("Проктика линейная ригресия")

print("Простая регрессия")
np.random.seed(42)
X_simple = np.random.rand(100, 1)*10
y_simple = 3 * X_simple.flatten() + 2 + np.random.randn(100) * 2

X_train, X_test, y_train, y_test = train_test_split(X_simple, y_simple, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"mse: {mse}")
print(f"mae: {mae}")
print(f"r2: {r2}")
print(f"Коефиценты coef: {model.coef_}")
print(f"Коефиценты intercept: {model.intercept_}")


plt.figure(figsize=(12,5))
plt.scatter(y_test, y_pred)
min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
plt.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Идеальное предсказание (y = x)')
plt.savefig('regression_predictions.png', dpi=150, bbox_inches='tight')
plt.show()