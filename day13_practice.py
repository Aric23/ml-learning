import pandas as pd 
import numpy as np

students = pd.DataFrame({
    'Имя': ['Алексей', 'Мария', 'Дмитрий', 'Елена', 'Сергей'],
    'Возраст': [20, 21, 19, 20, 22],
    'Специальность': ['Информатика', 'Математика', 'Физика', 'Информатика', 'Математика'],
    'Средний балл': [4.5, 4.8, 4.2, 4.9, 4.3]
})

students.to_csv('students.csv', index=False, encoding='utf-8')
print("Файл students.csv сохранён")

df_loaded = pd.read_csv('students.csv', encoding='utf-8')
print("read file:")
print(df_loaded)

print("DataFrame Equales:", students.equals(df_loaded))
