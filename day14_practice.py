import pandas as pd
import numpy as np





students = pd.DataFrame({
    'student_id': [1, 2, 3, 4],
    'name': ['Анна', 'Иван', 'Мария', 'Пётр']
})

grades = pd.DataFrame({
'student_id' : [1, 2, 1, 3, 2, 4],
'subject': ['Математика', 'Математика', 'Физика', 'Физика', 'Химия', 'Математика'],
'grade': [5, 4, 5, 4, 5, 3]
})

print("Студенты:")
print(students)
print("\nОценки:")
print(grades)

df_merged = pd.merge(students, grades, on='student_id')
print("\nОбъединённая таблица:")
print(df_merged)

avg_grade = df_merged.groupby('name')['grade'].mean()
print("\nСредний балл каждого студента:")
print(avg_grade)