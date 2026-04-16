import numpy as np 

print("Статический анализатор данных")

heights = np.random.normal(170, 10, 100)
print(f"Сгенерировано {len(heights)} значений роста")

print("Основные статистикаи: ")
print("Среднее: ", np.mean(heights))
print("Медиана: ", np.median(heights))
print("Стандартное отклонение: ", np.std(heights))
print("Минимум: ", np.min(heights))
print("Максимум: ", np.max(heights))

q1 = np.percentile(heights, 25)
q2 = np.percentile(heights, 50)
q3 = np.percentile(heights, 75)

print(f"\n📐 Квартили:")
print(f"  25-й процентиль: {q1:.1f} см")
print(f"  50-й процентиль (медиана): {q2:.1f} см")
print(f"  75-й процентиль: {q3:.1f} см")
print(f"\n🔍 Анализ:")
tall_people = heights[heights > 180]
short_people = heights[heights < 160]
print(f"  Людей выше 180 см: {len(tall_people)}")
print(f"  Людей ниже 160 см: {len(short_people)}")

z_scores = (heights - np.mean(heights)) / np.std(heights)
print(f"\n📊 Z-оценки:")
print(f"  Диапазон: от {np.min(z_scores):.2f} до {np.max(z_scores):.2f}")
print(f"  Стандартное отклонение Z-оценок: {np.std(z_scores):.2f}")

print(f"\n📊 Распределение роста:")
bins = [150, 160, 170, 180, 190, 200]
hist, _ = np.histogram(heights, bins=bins)
for i in range(len(bins)-1):
    bar = "#" * (hist[i] // 2)
    print(f"  {bins[i]}-{bins[i+1]} см: {bar} ({hist[i]})")