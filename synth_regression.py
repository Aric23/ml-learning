import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)
X = np.random.rand(200, 1 )*10

true_y =  2*X.flatten() + 1

noise_levels = [0, 1, 2, 5, 10]

plt.figure(figsize=(15,12))

for i, noise in enumerate(noise_levels, 1):
    y = true_y + np.random.randn(200)* noise

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    plt.subplot(2,3,i)
    plt.scatter(X_test, y_test, alpha=0.6, label='Тестовые данные')
    plt.plot(X_test, y_pred, 'r-', linewidth=2, label='Предсказание')
    plt.plot(X_test, 2*X_test.flatten()+1, 'g--', linewidth=2, label='Истинная линия')
    plt.title(f'Шум = {noise}\nMSE = {mse:.2f}, R² = {r2:.3f}')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('noise_impact.png', dpi=150)
plt.show()

print("Графики сохранены в 'noise_impact.png'")
print("Вывод: чем больше шум, тем хуже качество модели")

