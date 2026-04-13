tasks = [
    "Купить молоко",
    "Сделать домашнее задание",
    "Позвонить маме",
    "Пойти в спортзал"
]

with open("todo.txt", "w", encoding="utf-8") as f:
    for i, task in enumerate(tasks, 1):
        f.write(f"{i}. {task}\n")

print("Задачи сохранены в файл 'todo.txt'")

def read_and_display(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                print(f"{i}: {line.rstrip()}")
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден")
    except Exception as e:
        print(f"Ошибка: {e}")
        
read_and_display("todo.txt")
read_and_display("nonexistent.txt")


def copy_file(source, destination):
    """Копирует содержимое одного файла в другой"""
    try:
        with open(source, "r", encoding="utf-8") as src:
            content = src.read()
        
        with open(destination, "w", encoding="utf-8") as dst:
            dst.write(content)
        
        print(f"Файл скопирован: {source} → {destination}")
        return True
    except FileNotFoundError:
        print(f"Ошибка: исходный файл '{source}' не найден")
        return False
    except Exception as e:
        print(f"Ошибка при копировании: {e}")
        return False

copy_file("todo.txt", "todo_backup.txt")

import csv

# Данные для сохранения
data = [
    {"name": "Анна", "age": 25, "city": "Москва"},
    {"name": "Иван", "age": 30, "city": "СПб"},
    {"name": "Мария", "age": 28, "city": "Казань"}
]

with open("people.csv", "w", encoding="utf-8", newline="") as f:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("Люди старше 26 лет:")
    for row in reader:
        if int(row["age"]) > 26:
            print(f"  {row['name']} ({row['age']} лет) из {row['city']}")