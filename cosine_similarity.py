import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("КОСИНУСНОЕ РАССТОЯНИЕ: Сравнение текстов")
print("=" * 60)

# ========== 1. ПРЕДСТАВЛЯЕМ ТЕКСТЫ КАК ВЕКТОРЫ ==========
print("\n1. Векторное представление текстов:")

# Три текста (просто для примера)
# Словарь: ['яблоко', 'банан', 'апельсин']
text1 = [5, 1, 2]   # частота слов в тексте 1
text2 = [2, 4, 1]   # частота слов в тексте 2
text3 = [4, 2, 3]   # частота слов в тексте 3

print(f"Текст 1 (яблоко, банан, апельсин): {text1}")
print(f"Текст 2 (яблоко, банан, апельсин): {text2}")
print(f"Текст 3 (яблоко, банан, апельсин): {text3}")

# ========== 2. ВЫЧИСЛЯЕМ КОСИНУСНУЮ БЛИЗОСТЬ ==========
def cosine_similarity(v1, v2):
    """Вычисляет косинусную близость между двумя векторами"""
    v1 = np.array(v1)
    v2 = np.array(v2)
    dot = np.dot(v1, v2)
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    if norm1 == 0 or norm2 == 0:
        return 0
    return dot / (norm1 * norm2)

print("\n2. Косинусная близость:")
print(f"  Текст 1 vs Текст 2: {cosine_similarity(text1, text2):.3f}")
print(f"  Текст 1 vs Текст 3: {cosine_similarity(text1, text3):.3f}")
print(f"  Текст 2 vs Текст 3: {cosine_similarity(text2, text3):.3f}")

# ========== 3. ИНТЕРПРЕТАЦИЯ ==========
print("\n3. Интерпретация:")
print("Косинусная близость показывает, насколько похожи векторы:")
print("  1.0 → идентичные (одинаковые тексты)")
print("  0.5 → частично похожи")
print("  0.0 → совсем не похожи (перпендикулярны)")

# ========== 4. ВИЗУАЛИЗАЦИЯ В 2D ==========
# Для визуализации берём только первые два измерения
v1_2d = [text1[0], text1[1]]
v2_2d = [text2[0], text2[1]]
v3_2d = [text3[0], text3[1]]

plt.figure(figsize=(8, 8))

# Начало координат
origin = [0, 0]

# Рисуем векторы
plt.quiver(*origin, v1_2d[0], v1_2d[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Текст 1')
plt.quiver(*origin, v2_2d[0], v2_2d[1], angles='xy', scale_units='xy', scale=1, color='red', label='Текст 2')
plt.quiver(*origin, v3_2d[0], v3_2d[1], angles='xy', scale_units='xy', scale=1, color='green', label='Текст 3')

plt.xlim(-1, 7)
plt.ylim(-1, 6)
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)
plt.grid(True, alpha=0.3)
plt.legend()
plt.title('Векторное представление текстов (первые 2 признака)')
plt.xlabel('частота "яблоко"')
plt.ylabel('частота "банан"')
plt.show()

print("\n✅ Чем ближе векторы по направлению, тем более похожи тексты!")