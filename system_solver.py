import numpy as np

print("=" * 60)
print("РЕШАТЕЛЬ СИСТЕМ ЛИНЕЙНЫХ УРАВНЕНИЙ")
print("=" * 60)

def solve_system(A, b):
    n = A.shape[0]

    print(f"\nСистема {n}×{n}:")
    print(f"Матрица A:\n{A}")
    print(f"Вектор b: {b}")

    det = np.linalg.det(A)
    print(f"Определитель: {det:.4f}")

    if abs(det) < 1e-10:
        print("⚠️ Определитель близок к 0 → система не имеет единственного решения!")
        return None

    x = np.linalg.solve(A, b)

    print(f"Решение - {x}")
    check = A @ x 
    print(f"Проверка A×x: {check}")
    print(f"Должно быть {b}")

    return x

# ========== ИНТЕРАКТИВНЫЙ РЕЖИМ ==========

while True:
    print("\n" + "=" * 60)
    print("Введите размер системы (2 или 3), или 'exit' для выхода:")
    user_input = input("> ")
    
    if user_input.lower() == 'exit':
        print("До свидания!")
        break

    try:
        n = int(user_input)
        if n not in [2,3]:
            print("Поддерживаются только системы 2×2 и 3×3")
            continue

        
        print(f"\nВведите коэффициенты матрицы A ({n} строк, {n} столбцов):")
        A = np.zeros((n,n))
        for i in range(n):
            row = input(f"Строка {i+1} (через пробел): ").split()
            if len(row) != n:
                print(f"Нужно {n} чисел!")
                continue
            A[i] = [float(x) for x in row]

        print(f"\nВведите свободные члены b ({n} чисел):")
        b_str = input("> ").split()
        if len(b_str) !=n:
            print(f"Нужно {n} чисел!")
            continue
        
        b = np.array([float(x) for x in b_str])

        solve_system(A, b)

    except ValueError:
        print("Ошибка: введите числа!")
    except np.linalg.LinAlgError:
        print("")


