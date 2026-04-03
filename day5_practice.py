n = int(input("Введите N - "))
total = 0

for i in range(1, n+1):
    total = total + i

print(f"Сумма чисел от 1 до {n} = {total}")

f = int(input("Введите число: "))
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print(f"{n}! = {factorial}")

print("Чётные числа:")
for i in range(2, n + 1, 2):
    print(i, end=" ")  # end=" " печатает в одну строку
print()  # перевод строки


correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin = input("Введите пин-код: ")
    if pin == correct_pin:
        print("Доступ разрешён!")
        break
    else:
        attempts = attempts - 1
        print(f"Неверно. Осталось попыток: {attempts}")

if attempts == 0:
    print("Доступ заблокирован.")