year = int(input("введите номер месяца 1-12:"))


if year == 12 or year == 1 or year == 2:
    print("Зима")
elif year == 3 or year == 4 or year == 5:
    print("Весна")
elif year == 6 or year == 7 or year == 8:
    print("Лето")
elif year == 9 or year == 10 or year == 11:
    print("Осень")
else:
    print("Ошибка")

chai = float(input("введите сумму счеиа:"))
level = input("Уровень обслуживания - ")
chai1 = 0
if level == "отлично":
   chai1 = chai * 0.2
elif level == "хорошо":
    chai1 = chai * 0.15
elif level == "плохо":
    chai1 = chai * 0.05
else:
    print("Ошибка")

print(f"чай {chai1}, общая сумма - {chai}")
 
a1 = int(input("Введите первую сторону треугольника - :"))
a2 = int(input("Введите вторую сторону треугольника - :"))
a3 = int(input("Введите третью сторону треугольника - :"))

if (a1 < (a2+a3)) and (a2 < (a1+a3)) and (a3 < (a2+a1)):
    print("Треугольник существует")
else:
    print("Треугольник не существует")