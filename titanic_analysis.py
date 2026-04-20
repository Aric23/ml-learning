import pandas as pd
import numpy as np

print("🚢 Анализ датасета Titanic")

try:
    import seaborn as sns
    titanic = sns.load_dataset('titanic')
    print('Sucsess')
except:
    print("Seaborn isnt loading, created demo version")
    titanic = pd.DataFrame({
        'survived': [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        'pclass': [3, 1, 3, 1, 2, 3, 1, 3, 2, 3],
        'sex': ['male', 'female', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male'],
        'age': [22, 38, 26, 35, 35, 27, 54, 2, 28, 19],
        'fare': [7.25, 71.28, 7.92, 53.10, 8.05, 8.66, 51.86, 21.08, 11.13, 30.50]
    })

print(f"Датасет содержит {titanic.shape[0]} строк и {titanic.shape[1]} столбцов")
print("\nПервые 5 строк:")
print(titanic.head())

print("\n" + "="*50)
print("1. ОБЩАЯ ИНФОРМАЦИЯ")
print("="*50)
print(titanic.info())

print("\n" + "="*50)
print("2. СТАТИСТИКА ПО ЧИСЛОВЫМ КОЛОНКАМ")
print("="*50)
print(titanic.describe())

print("\n" + "="*50)
print("3. АНАЛИЗ ВЫЖИВАЕМОСТИ")
print("="*50)


survival_rate = titanic['survived'].mean() * 100
print(f"Общий процент выживших: {survival_rate:.1f}%")

print("\nВыживаемость по классу билета:")
pclass_survival = titanic.groupby('pclass')['survived'].mean() * 100
print(pclass_survival)
for pclass, rate in pclass_survival.items():
    print(f"  Класс {pclass}: {rate:.1f}%")

print("\nВыживаемость по полу:")
sex_survival = titanic.groupby('sex')['survived'].mean() * 100
for sex, rate in sex_survival.items():
    print(f"  {sex.capitalize()}: {rate:.1f}%")

print("\n" + "="*50)
print("4. ФИЛЬТРАЦИЯ ДАННЫХ")
print("="*50)

children = titanic[titanic['age'] < 18]
print(f"Детей на корабле: {len(children)}")
if len(children) > 0:
    child_survival = children['survived'].mean() * 100
    print(f"Процент выживших детей: {child_survival:.1f}%")

first_class = titanic[titanic['pclass'] == 1]
print(f"\nПассажиров первого класса: {len(first_class)}")
print(f"Из них выжило: {first_class['survived'].sum()}")

print("\n" + "="*50)
print("5. САМЫЕ ДОРОГИЕ БИЛЕТЫ")
print("="*50)
most_expensive = titanic.nlargest(5, 'fare')
print(most_expensive[['pclass', 'sex', 'age', 'fare', 'survived']])

print("\n" + "="*50)
print("6. КОРРЕЛЯЦИИ")
print("="*50)
numeric_cols = titanic.select_dtypes(include=[np.number])
print(numeric_cols.corr()['survived'].sort_values(ascending=False))

print("\n📊 Анализ завершён!")