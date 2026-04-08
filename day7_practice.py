empty = {}
empty = dict()

user1 = dict(name ="Anna", age =30)
product = {"id": 1, "price": 99.99}

print(user1["name"])

print(user1.get("email"))
print(user1.get("email", "no"))

user = {"name": "Ivan", "age": 25}

user["city"] = "Moscow"
print(user)

user["age"] = 26
print(user)

del user["age"]
print(user)

city = user.pop("city")
print(city)
print(user)

key, value = user.popitem()
print(key, value)

user.clear()
print(user)

person1 = {
   "name": "Ольга",
   "age": 28,
   "job": "инженер",
   "city": "Москва"
}

for key in person1:
    print(key)

for key in person1:
    print(f"Ключ: {key}, Значение: {person[key]}")


for key, value in person1.items():
    print(f"{key} = {value}")


for key, value in person1.items():
    print(f"{key} = {value}")

person = {"name": "Алексей", "age": 30, "city": "СПб"}

print(person.keys())
print(person.values())
print(person.items())

print("name" in person)
print("phon" in person)

print(len(person))
extra = {"phone": "123-456", "email": "alex@mail.com"}
person.uptade(extra)
print(person)

fruits = {"яблоко", "банан", "апельсин"}
numbers = set([1, 2, 3, 2, 1])
empty_set = set()
fruits.add("mango")
print(fruits)
fruits.remove("банан")
fruits.discard("киви")
print("яблоко" in fruits)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(a.union(b))
print(a & b)  # {3, 4}
print(a.intersection(b))
print(a - b)  # {1, 2}
print(a.difference(b))
print(a ^ b)

phone_book = {}

print("📞 Телефонная книга")
print("Команды: add, get, delete, list, exit")

while True:
   command = input("Введите команду: ").strip().lower()


   if command == "exit":
       print("До свидания!")
        break

   elif command == "add":
      name = input("Имя: ")
      phone = input("Телефон: ")
      phone_book[name]  = phone
      print(f"✅ Добавлен: {name} -> {phone}")
   
   elif command == "get":
      name = input("Чей номер ищем? - ")
      if name in phone_book:
         print(f"📱 {name}: {phone_book[name]}")
      else:
          print(f"❌ {name} не найден(а)")
   
   elif command == "delete":
      name = input("Кого удаляем - ")
      if name in phone_book:
         delete = phone_book.pop(name)
         print(f"🗑️ Удалён: {name} -> {deleted}")
      else:
         print(f"❌ {name} не найден(а)")

   elif command == "list":
      if not phone_book:
         print("📭 Телефонная книга пуста")
      else:
         for name, value in phone_book.items():
             print(f"  {name}: {phone}")
   
   else:
    print("❌ Неизвестная команда")



text = "кот собака кот кот рыба собака кот рыба рыба рыба"
print("Текст:", text)
words = text.split()
word_count = {}
for word in words:
   if word in word_count:
      word_count[word] += 1
   else:
      word_count[word] = 1

print("\n📊 Частота слов:")
for word, count in word_count.items():
    print(f"  {word}: {count} раз(а)")

unique_words = set(words)
print(f"\n🔤 Уникальных слов: {len(unique_words)}")
print(f"Уникальные слова: {unique_words}")
most_common = max(word_count, )

most_common = max(word_count, key=word_count.get)
print(f"\n🏆 Самое частое слово: '{most_common}' ({word_count[most_common]} раз)")


python_students = {"Анна", "Иван", "Мария", "Пётр"}
java_students = {"Иван", "Ольга", "Пётр", "Сергей"}

print("🐍 Python:", python_students)
print("☕ Java:", java_students)

both = python_students & java_students
print(f"\n🔄 Учатся на обоих курсах: {both}")

only_python = python_students - java_students
print(f"🐍 Только Python: {only_python}")
 Студенты, которые учатся только на Java
only_java = java_students - python_students
print(f"☕ Только Java: {only_java}")
all_students = python_students | java_students
print(f"\n👥 Всего студентов: {len(all_students)}")
print(f"Список: {all_students}")
         