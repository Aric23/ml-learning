import pandas as pd
import numpy as np 

print("Анализ продаж магазина")

np.random.seed(42)
dates = pd.date_range('2024-01-01', '2024-03-31', freq='D')
products = ['Телефон', 'Ноутбук', 'Планшет', 'Наушники', 'Зарядка']

import pandas as pd
import numpy as np

print("📊 АНАЛИЗ ПРОДАЖ МАГАЗИНА")
print("="*50)

# Генерируем данные о продажах
np.random.seed(42)
dates = pd.date_range('2024-01-01', '2024-03-31', freq='D')
products = ['Телефон', 'Ноутбук', 'Планшет', 'Наушники', 'Зарядка']

data = []
for date in dates:
    for product in products:
        # Вероятность продажи в выходные выше
        is_weekend = date.dayofweek >= 5
        prob = 0.7 if is_weekend else 0.4
        if np.random.random() < prob:
            quantity = np.random.randint(1, 5)
            price = {
                'Телефон': 50000,
                'Ноутбук': 80000,
                'Планшет': 30000,
                'Наушники': 5000,
                'Зарядка': 1500
            }[product]
            data.append({
                'Дата': date,
                'Товар': product,
                'Количество': quantity,
                'Цена': price,
                'Выручка': quantity * price,
                'День_недели': date.day_name()
            })

df = pd.DataFrame(data)
print(f"Сгенерировано {len(df)} продаж")
print("\nПервые 5 строк:")
print(df.head())

# ========== 1. Общая статистика ==========
print("\n" + "="*50)
print("1. ОБЩАЯ СТАТИСТИКА")
print("="*50)

total_revenue = df['Выручка'].sum()
total_items = df['Количество'].sum()
avg_check = total_revenue / len(df)

print(f"Общая выручка: {total_revenue:,.0f} руб.")
print(f"Всего продано товаров: {total_items}")
print(f"Средний чек: {avg_check:,.0f} руб.")

# ========== 2. Анализ по товарам ==========
print("\n" + "="*50)
print("2. АНАЛИЗ ПО ТОВАРАМ")
print("="*50)

product_stats = df.groupby('Товар').agg({
    'Выручка': 'sum',
    'Количество': 'sum',
    'Товар': 'count'
}).rename(columns={'Товар': 'Количество_продаж'})

product_stats['Доля_выручки'] = product_stats['Выручка'] / total_revenue * 100
print(product_stats.sort_values('Выручка', ascending=False))

# ========== 3. Анализ по дням недели ==========
print("\n" + "="*50)
print("3. АНАЛИЗ ПО ДНЯМ НЕДЕЛИ")
print("="*50)

weekday_stats = df.groupby('День_недели')['Выручка'].sum()
print(weekday_stats.sort_values(ascending=False))

# ========== 4. Обработка пропусков ==========
print("\n" + "="*50)
print("4. ОБРАБОТКА ПРОПУСКОВ")
print("="*50)

# Создаём DataFrame с пропусками для демонстрации
df_with_na = df.copy()
df_with_na.loc[df_with_na.sample(10).index, 'Количество'] = np.nan
print(f"Пропусков в 'Количество': {df_with_na['Количество'].isna().sum()}")

# Заполняем пропуски медианой
median_quantity = df_with_na['Количество'].median()
df_with_na['Количество'] = df_with_na['Количество'].fillna(median_quantity)
print(f"Заполнено медианой: {median_quantity}")

# ========== 5. Топ-5 дней по выручке ==========
print("\n" + "="*50)
print("5. ТОП-5 ДНЕЙ ПО ВЫРУЧКЕ")
print("="*50)

top_days = df.groupby('Дата')['Выручка'].sum().nlargest(5)
for date, revenue in top_days.items():
    print(f"{date.strftime('%Y-%m-%d')}: {revenue:,.0f} руб.")

print("\n📊 Анализ завершён!")