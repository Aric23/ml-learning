print("📊 Таблица умножения от 1 до 10\n")

for i in range(1, 11):
    print(f"--- Таблица умножения на {i} ---")
    for j in range(1, 11):
        print(f"{i} × {j} = {i * j}")
    print()  # пустая строка между таблицами