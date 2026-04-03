print("Вводи числа (отрицательное число для завершения):")

total = 0
count = 0

while True:
    num = float(input("Число: "))
    if num < 0:
        break
    total = total + num
    count = count + 1

if count > 0:
    print(f"Введено положительных чисел: {count}")
    print(f"Сумма: {total}")
    print(f"Среднее: {total / count}")
else:
    print("Не введено ни одного положительного числа")