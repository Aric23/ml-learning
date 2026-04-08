original = {"a": 1, "b": 2, "c": 1}
print("Исходный словарь:", original)

# Пустой словарь для результата
inverted = {}

# Перебираем все пары (ключ, значение) в исходном словаре
for key, value in original.items():
    # Если такого значения ещё нет в новом словаре
    if value not in inverted:
        # Создаём для него пустой список
        inverted[value] = []
    
    # Добавляем текущий ключ в список для этого значения
    inverted[value].append(key)

print("Инвертированный словарь:", inverted)

a = set([1, 2, 3, 5, 8, 2, 7, 3, 8, 2, 4])
b = set([3, 5, 7, 2, 5, 8, 3, 4, 5, 8])

c = a & b
print(c)

words = input("Введите строку - ")

import string
 
for punct in string.punctuation:
     words = words.replace(punct, " ")

     word = words.lower().split()

     if not word:
        print("❌ Текст не содержит слов")
        continue



vowels = set("аеёиоуыэюя")
print("Гласные буквы:", vowels)

# Запрашиваем строку
text = input("Введите строку: ").strip().lower()
print(f"Вы ввели: '{text}'")

# Счётчики
vowel_count = 0
consonant_count = 0

# Проходим по каждому символу
for char in text:
    if char in vowels:
        # Если буква гласная
        vowel_count += 1
    elif char.isalpha():  # Проверяем, что это буква (и не гласная → согласная)
        consonant_count += 1
    # Остальные символы (пробелы, цифры, знаки) игнорируем

print(f"\n📊 Результат:")
print(f"  Гласных: {vowel_count}")
print(f"  Согласных: {consonant_count}")
print(f"  Всего букв: {vowel_count + consonant_count}")

product1 = {}

print("Продукты")
print("Команды: add, get, delete, list, exit")
total = 0
while True:
   command = input("Введите команду: ").strip().lower()


   if command == "exit":
      print("До свидания!")
      break

   elif command == "add":
      product = input("Продукт: ")
      price = input("Цена: ")
      product1[product]  = price
      print(f"✅ Добавлен: {product} -> {price}")
   
   elif command == "get":
      if not product1:
         print(f"продуктов нету")
      else:
          for value in product1.values():
            total += value

   
   elif command == "delete":
      name = input("Кого удаляем - ")
      if name in product1:
         delete = product1.pop(name)
         print(f"🗑️ Удалён: {name} -> {delete}")
      else:
         print(f"❌ {name} не найден(а)")

   elif command == "list":
      if not product1:
         print("Продуктов нету")
      else:
         for name, value in product1.items():
             print(f"  {name}: {value}")
   
   else:
    print("❌ Неизвестная команда")