print("🧮 Умный калькулятор")
print("Доступные операции:")
print("  +  сложение")
print("  -  вычитание")
print("  *  умножение")
print("  /  деление")
print("  ** возведение в степень")
print("  %  остаток от деления")

num1 = float(input("Введите первое число - "))
operation = input("Введите операцию (+, -, *, /, **, %)")
num2 = float(input("Введите второе число: "))

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
        print("❌ Ошибка: деление на ноль!")
elif operation == "**":
    result = num1 ** num2
    print(f"{num1} ** {num2} = {result}")
elif operation == "%":
    if num2 != 0:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
    else:
        print("❌ Ошибка: деление на ноль!")
else:
    print("❌ Неизвестная операция")