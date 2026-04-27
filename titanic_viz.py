import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("🚢 Анализ Titanic с визуализацией")

try:
    import seaborn as sns
    titanic = sns.load_dataset('titanic')
    print("Датасет загружен из seaborn")
except:
    # Создаём демо-данные
    np.random.seed(42)
    n = 500
    titanic = pd.DataFrame({
        'survived': np.random.choice([0, 1], n, p=[0.62, 0.38]),
        'pclass': np.random.choice([1, 2, 3], n, p=[0.24, 0.21, 0.55]),
        'sex': np.random.choice(['male', 'female'], n, p=[0.65, 0.35]),
        'age': np.random.normal(30, 15, n),
        'fare': np.random.exponential(30, n)
    })
    titanic.loc[titanic['age'] < 0, 'age'] = 0

fig = plt.figure(figsize=(15, 12))

ax1 = fig.add_subplot(2, 2, 1)
survival_by_class = titanic.groupby('pclass')['survived'].mean() * 100
ax1.bar(survival_by_class.index, survival_by_class.values, color=['gold', 'silver', '#CD7F32'])
ax1.set_title('Выживаемость по классу билета (%)', fontsize=12)
ax1.set_xlabel('Класс билета')
ax1.set_ylabel('Процент выживших')
for i, v in enumerate(survival_by_class):
    ax1.text(i+1 , v , f'{v:.1f}%', ha='center')

ax2 = fig.add_subplot(2, 2, 2)
survival_by_sex = titanic.groupby('sex')['survived'].mean() * 100
ax2.bar(survival_by_sex.index, survival_by_sex.values, color=['lightblue', 'pink'])

ax2.set_title('Выживаемость по полу (%)', fontsize=12)
ax2.set_xlabel('Пол')
ax2.set_ylabel('Процент выживших')

for i , v, in enumerate(survival_by_sex.values):
    ax2.text(i, v+1,  f'{v:.1f}%', ha='center')

ax3 = fig.add_subplot(2, 2, 3)
survived_age = titanic[titanic['survived'] == 1]['age'].dropna()
died_age = titanic[titanic['survived'] == 0]['age'].dropna()

ax3.hist([survived_age, died_age], bins=20, alpha=0.7,
label=['Выживание', 'Погибшие'], color=['green', 'red'])
ax3.set_title('Распределение возраста', fontsize=12)
ax3.set_xlabel('Возраст')
ax3.set_ylabel('Количество')
ax3.legend()

ax4 = fig.add_subplot(2,2,4)
colors = titanic['survived'].map({0: 'red', 1: 'green'})
ax4.scatter(titanic['age'], titanic['fare'], c=colors, alpha=0.5, s=30)
ax4.set_title('Возраст vs Стоимость билета (зелёные — выжившие)', fontsize=12)
ax4.set_xlabel('Возраст')
ax4.set_ylabel('Стоимость билета')
ax4.set_ylim(0, 200)

plt.tight_layout()
plt.savefig('titanic_analysis.png', dpi=150, bbox_inches='tight')
plt.show()