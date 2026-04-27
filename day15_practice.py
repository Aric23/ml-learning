import matplotlib.pyplot as plt
import numpy as np



days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
temp_morning =[15, 16, 14, 17, 18, 20, 19]
temp_evening = [12, 13, 11, 14, 15, 17, 16]
plt.figure(figsize=(10, 6))
plt.plot(days, temp_morning, 'ro-', linewidth=2, markersize=8, label='Утро')
plt.plot(days, temp_evening, 'bs--', linewidth=2, markersize=8, label='Вечер')
plt.title('Температура в течение недели', fontsize=14)
plt.xlabel('День недели', fontsize=12)
plt.ylabel('Температура (°C)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.ylim(10, 22)

for i, (m, e) in enumerate(zip(temp_morning, temp_evening)):
    plt.text(i, m + 0.5, f'{m}°', ha='center', fontsize=9)
    plt.text(i, e - 1, f'{e}°', ha='center', fontsize=9)

plt.show()

np.random.seed(42)
heights = np.random.normal(170, 10, 100)
weights = 0.7 * (heights - 150) + np.random.normal(0, 5, 100)

plt.figure(figsize=(10, 6))
plt.scatter(heights, weights, c=heights, cmap='viridis', s=50, alpha=0.7)
plt.colorbar(label='Рост (см)')

plt.title('Зависимость веса от роста', fontsize=14)
plt.xlabel('Рост (см)', fontsize=12)
plt.ylabel('Вес (кг)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()  

subjects  = ['Математитика', 'Физика','Информатика','Химия ','Биология']
grades = [4.5, 4.2, 4.8, 3.9, 4.1]

plt.figure(figsize=(10, 6))
bars = plt.bar(subjects, grades, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
plt.title('Средние оценки по предметам', fontsize=14)
plt.xlabel('Предмет', fontsize=12)
plt.ylabel('Средний балл', fontsize=12)
plt.ylim(0, 5)
plt.grid(True, alpha=0.3, axis='y')

for bar, grade in zip(bars, grades):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
             f'{grade}', ha='center', fontsize=10 )

plt.show()

x = np.linspace(-5, 5, 100)
y = x**3 - 3*x
 
plt.figure(figsize=(10,6))
plt.plot(x,y,'g-', linewidth=2, label='f(x) = x³ - 3x')
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)
plt.title('Кубическая функция', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig('cubic_function.png', dpi=150, bbox_inches='tight')
plt.savefig('cubic_function.pdf', bbox_inches='tight')
print("График сохранён в файлы: cubic_function.png и cubic_function.pdf")
plt.show()