print("📚 Анализатор текста")
print("Введите текст (или 'exit' для выхода):")

while True:
    text = input("\nТекст: ").strip()

    if text.lower() == "exit":
        print("До свидания!")
        break
    
    if not text:
        print("❌ Введите непустой текст")
        continue

    import string

     for punct in string.punctuation:
        text = text.replace(punct, " ")

     words = text.lower().split()

     if not words:
        print("❌ Текст не содержит слов")
        continue

    word_count = len(words)
    unique_count = len(set(words))

    print(f"\n📊 Статистика:")
    print(f"  Слов всего: {word_count}")
    print(f"  Уникальных слов: {unique_count}")

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

     sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print(f"\n🏆 Топ-5 самых частых слов:")
    for i, (word, count) in enumerate(sorted_words[:5], 1):
        print(f"  {i}. {word}: {count} раз(а)")
    
    # Длина слов
    avg_length = sum(len(word) for word in words) / word_count
    longest = max(words, key=len)
    
    print(f"\n📏 Анализ слов:")
    print(f"  Средняя длина слова: {avg_length:.1f}")
    print(f"  Самое длинное слово: '{longest}' ({len(longest)} букв)")
