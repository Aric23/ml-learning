def create_user(username, **info):
    user = {"username" : username}
    user.update(info)
    return user

user1 = create_user("alex123", age=25, city="Москва")
user2 = create_user("maria", email="maria@mail.ru", is_active=True)

print(user1)
print(user2)

def universal_function(*args, **kwargs):
    print("Position ards:", args)
    print("named argd:", kwargs)

universal_function(1,2,3, name="Anna", age=25)

def sq(x):
    return x**2

square_lambda = lambda x: x ** 2
print(square_lambda(5))        # 25
print(square_lambda(5))

add = lambda a, b: a + b
print(add(3, 5))

print((lambda x, y: x * y )(4, 5))

students = [("Анна", 85), ("Иван", 92), ("Мария", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)

def make_multiplier(factor):
    """Создаёт функцию, умножающую число на factor"""
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

   # 10
print(triple(5))   # 15

def average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

print(average(10, 20, 30))     # 20.0
print(average(5, 15))          # 10.0
print(average())       

def create_profile(name, **info):
    profile = {"name" : name}
    for key, value in info.items():
        profile[key] = value
    return profile
    
profile1 = create_profile("Анна", age=25, city="Москва", job="инженер")
profile2 = create_profile("Иван", hobby="футбол", age=30)

print(profile1)
print(profile2)

books = [
    ("Война и мир", 1869, 4.8),
    ("Преступление и наказание", 1866, 4.7),
    ("Мастер и Маргарита", 1967, 4.9),
    ("Евгений Онегин", 1833, 4.6)
]

by_year = sorted(books, key=lambda book: book[1])
print("По году:", by_year)

by_rating = sorted(books, key=lambda book: book[2], reverse=True)
print("По рейтингу:", by_rating)

by_title_length = sorted(books, key=lambda book: len(book[0]))
print("По длине названия:", by_title_length)

def make_power(exponent):
    """Создаёт функцию возведения в степень exponent"""
    def power(base):
        return base ** exponent
    return power

square = make_power(2)
cube = make_power(3)
fourth = make_power(4)

print(f"5 в квадрате: {square(5)}")      # 25
print(f"3 в кубе: {cube(3)}")           # 27
print(f"2 в 4-й степени: {fourth(2)}")  # 16

def log_call(func_name, *args, **kwargs):
    """Логирует вызов функции"""
    print(f"Вызов функции: {func_name}")
    print(f"  Позиционные аргументы: {args}")
    print(f"  Именованные аргументы: {kwargs}")
    return f"Функция {func_name} выполнена"

result = log_call("calculate", 10, 20, operation="sum", verbose=True)
print(result)