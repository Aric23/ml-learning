import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

print("=" * 60)
print("СЕГМЕНТАЦИЯ КЛИЕНТОВ")
print("=" * 60)

np.random.seed(42)
n_customers = 300

age = np.random.randint(18, 70, n_customers)
income = np.random.normal(50000, 20000, n_customers)
spending_score = np.random.normal(50, 20, n_customers)

df = pd.DataFrame({
    'Возраст': age,
    'Доход': income,
    'Траты': spending_score
})

print("Созданы данные о клиентах:")
print(df.head())
print(f"\nРазмер: {df.shape}")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

print("\nДанные масштабированы (среднее = 0, отклонение = 1)")


inertia = []
K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(K_range, inertia, 'bo-')
plt.xlabel('K (количество сегментов)')
plt.ylabel('Inertia')
plt.title('Метод локтя')
plt.grid(True, alpha=0.3)

k = 4  # выбрали по методу локтя
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
df['Сегмент'] = kmeans.fit_predict(X_scaled)
print("\nАнализ сегментов:")
for i in range(k):
    segment = df[df['Сегмент'] == i]
    print(f"\nСегмент {i}: {len(segment)} клиентов")
    print(f"  Средний возраст: {segment['Возраст'].mean():.1f}")
    print(f"  Средний доход: {segment['Доход'].mean():.0f}")
    print(f"  Средние траты: {segment['Траты'].mean():.1f}")

plt.subplot(1, 2, 2)
colors = ['blue', 'red', 'green', 'orange']
for i in range(k):
    segment = df[df['Сегмент'] == i]
    plt.scatter(segment['Доход'], segment['Траты'], 
                color=colors[i], alpha=0.6, label=f'Сегмент {i}')
                
plt.xlabel('Доход')
plt.ylabel('Траты')
plt.title('Сегментация клиентов')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('customer_segmentation.png', dpi=150)
plt.show()

print("\n✅ Сегментация завершена!")