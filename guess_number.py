import random

print("🎲 Игра 'Угадай число'!")
print("Я загадал число от 1 до 10. Попробуй угадать!")

secret_number = random.randint(1,10)

guess = int(input("Твое предложение: "))

if guess == secret_number:
     print("🎉 Поздравляю! Ты угадал!")
elif guess < secret_number:
     print(f"📈 Загаданное число больше, чем {guess}")
else:
    print(f"📉 Загаданное число меньше, чем {guess}")


print(f"Было загадано число {secret_number}")