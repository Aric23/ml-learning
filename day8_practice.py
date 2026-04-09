def greet_user(name):
    print(f"Привет, {name}!  Welcome")

greet_user("Alex")
greet_user("Maria")

def rectangle(width, height):
    return width * height

def circle_area(radius):
    return 3.14159 * radius **2

print(f"Площадь прямоугольника 5х3: {rectangle_area(5, 3)}")
print(f"Площадь круга радиусом 4: {circle_area(4)}")



def is_even(number):
    return number % 2 == 0


def is_positive(number):
    return number > 0


print(is_even(4))
print(is_even(7))
print(is_positive(5))
print(is_positive(-3))

def compare_numbers(a, b):
    if a > b:
        return f"{a} больше {b}"
    elif a < b:
        return f"{b} больше {a}"
    else:
        return f"{a} равно {b}"

print(compare_numbers(10, 5))
print(compare_numbers(3, 7))
print(compare_numbers(4, 4))


def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(3, 3))
print(power(2, 4))

def get_stats(numbers):
    total = sum(numbers)
    minumum = min(numbers)
    maximum = max(numbers)
    average = total / len(numbers)
    return total, minimum, maximum, average


scores = [5, 75, 4, 35, 654, 64, 65]
total, min_score, max_score, avg = get_stats(scores)

print(f"Сумма - {total}")
print(f"Мин - {minimum}")
print(f"Макс - {maximum}")
print(f"Среднее - {average}")


