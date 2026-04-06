movies = ["Begin", "Matric", "Titanic", "Avatar", "Gladiator"]
print("My films:", movies)

movies.append("Interster")
print("After adding:", movies)

movies.insert(1, "Forest Gamp")
print("After add:", movies)

last_movies = movies.pop()
print(f"Delet film {last_movies}")
print("After delet", movies)

movies.sort()
print("Отсортировано:", movies)

print("Матрица в списке:", "Матрица" in movies)


numbers = list(range(1, 11))
print("Исходный список:", numbers)

print(f"Первый: {numbers[0]}")
print(f"Третий: {numbers[2]}")
print(f"Последний: {numbers[-1]}")

print("Первые 5:", numbers[:5])
print("С 3 по 7:", numbers[2:7])
print("Чётные:", numbers[1::2])

total = sum(numbers)  # встроенная функция sum()
print(f"Сумма: {total}")


print(f"Максимум: {max(numbers)}")
print(f"Минимум: {min(numbers)}")

weekdays = ("ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС")
print("Дни недели:", weekdays)

print(f"Первый: {weekdays[0]}")
print(f"Последний: {weekdays[-1]}")

try: 
    weekdays[0] = "Monday"
except TypeError as e:
    print(f"Ошибка (как и ожидалось): {e}")

weekdays_list = list(weekdays)
print("Список из кортежа:", weekdays_list)

weekdays_list[0] = "Понедельник"
print("Изменённый список:", weekdays_list)


grades = [5, 4, 3, 5, 4, 5, 2, 4, 3, 5]
print("Оценки:", grades)

# Найди сумму вручную (без sum())
total = 0
for grade in grades:
    total = total + grade
print(f"Сумма оценок: {total}")

# Найди среднее арифметическое
average = total / len(grades)
print(f"Средний балл: {average:.2f}")

# Найди количество пятёрок
count_5 = 0
for grade in grades:
    if grade == 5:
        count_5 = count_5 + 1
print(f"Количество пятёрок: {count_5}")

# Найди количество оценок выше 3
count_good = 0
for grade in grades:
    if grade > 3:
        count_good = count_good + 1
print(f"Оценок выше 3: {count_good}")