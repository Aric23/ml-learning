# Гибкий калькулятор

def calculate(operation, *numbers):
    """
    Выполняет операцию над списком чисел.
    operation: 'sum', 'multiply', 'average', 'max', 'min'
    """
    if not numbers:
        return 0
    
    if operation == "sum":
        return sum(numbers)
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
        return result
    elif operation == "average":
        return sum(numbers) / len(numbers)
    elif operation == "max":
        return max(numbers)
    elif operation == "min":
        return min(numbers)
    else:
        return "Неизвестная операция"

# Демонстрация работы
print("🔢 Гибкий калькулятор")
print(f"Сумма: {calculate('sum', 1, 2, 3, 4, 5)}")
print(f"Произведение: {calculate('multiply', 2, 3, 4)}")
print(f"Среднее: {calculate('average', 10, 20, 30, 40)}")
print(f"Максимум: {calculate('max', 5, 8, 3, 12, 6)}")
print(f"Минимум: {calculate('min', 5, 8, 3, 12, 6)}")

# Интерактивный режим
print("\n--- Интерактивный режим ---")
print("Введите операцию и числа через пробел")
print("Пример: sum 10 20 30")
print("Доступные операции: sum, multiply, average, max, min")

while True:
    user_input = input("\n> ").strip()
    if user_input.lower() == "exit":
        print("До свидания!")
        break
    
    parts = user_input.split()
    if len(parts) < 2:
        print("Ошибка: нужно указать операцию и хотя бы одно число")
        continue
    
    operation = parts[0].lower()
    numbers = []
    for p in parts[1:]:
        try:
            numbers.append(float(p))
        except ValueError:
            print(f"Ошибка: '{p}' не является числом")
            break
    else:
        result = calculate(operation, *numbers)
        print(f"Результат: {result}")