# calculator.py

print("🔢 Простой калькулятор")

# Ввод чисел
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Ввод операции
operation = input("Выберите операцию (+, -, *, /): ")

# Вычисление и вывод результата
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Ошибка: деление на ноль!")
else:
    print("Неизвестная операция")