def celsius_to_fahrenheit(celsius):
    """Конвертирует градусы Цельсия в Фаренгейты"""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Конвертирует градусы Фаренгейта в Цельсии"""
    return (fahrenheit - 32) * 5/9

def km_to_miles(km):
    """Конвертирует километры в мили"""
    return km * 0.621371

def miles_to_km(miles):
    """Конвертирует мили в километры"""
    return miles / 0.621371

def kg_to_pounds(kg):
    """Конвертирует килограммы в фунты"""
    return kg * 2.20462

def pounds_to_kg(pounds):
    """Конвертирует фунты в килограммы"""
    return pounds / 2.20462

# Интерактивный режим
print("🔄 Конвертер единиц")
print("Доступные конвертации:")
print("  1. Цельсий → Фаренгейт")
print("  2. Фаренгейт → Цельсий")
print("  3. Километры → Мили")
print("  4. Мили → Километры")
print("  5. Килограммы → Фунты")
print("  6. Фунты → Килограммы")

choice = input("\nВыберите конвертацию (1-6): ")
value = float(input("Введите значение: "))

if choice == "1":
    result = celsius_to_fahrenheit(value)
    print(f"{value}°C = {result:.2f}°F")
elif choice == "2":
    result = fahrenheit_to_celsius(value)
    print(f"{value}°F = {result:.2f}°C")
elif choice == "3":
    result = km_to_miles(value)
    print(f"{value} км = {result:.2f} миль")
elif choice == "4":
    result = miles_to_km(value)
    print(f"{value} миль = {result:.2f} км")
elif choice == "5":
    result = kg_to_pounds(value)
    print(f"{value} кг = {result:.2f} фунтов")
elif choice == "6":
    result = pounds_to_kg(value)
    print(f"{value} фунтов = {result:.2f} кг")
else:
    print("Неверный выбор!")