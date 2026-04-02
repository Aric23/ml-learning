num = int(input("Введите число  - "))

if num % 2 == 0:
    print(f"Число {num} четное")
else:
    print(f"Число {num} нечетное")



age = int(input("Сколько тебе лет? - "))

if age < 0:
    print("Ошибка, возраст не может быть отрицательным")
elif age < 3:
    print("Маладенец")
elif age <12: 
    print("Ребенок")
elif age < 18:
    print("Подросток")
elif age < 60:
    print("Взрослый")
else: 
    print("Пожилой")


correct_password = "python123"
user_password = input("Введите пароль - ")\

if user_password == correct_password:
    print("Доступ разрешен")
else:
    print("Неверный пароль")



temperature = int(input("Температура на улице - "))
is_raining = input("Идет дождь, (да/нет) - ")

if temperature < 0:
    print("Оденься очень тепло, на улице мороз")
elif temperature < 10:
    if is_raining == "да":
        print("Холодно и дождливо. Надень куртку и возьми зонт")
    else:
         print("Прохладно, надень куртку")
elif temperature < 20:
     print("Тепло, можно надеть лёгкую куртку")
else:
    if is_raining == "да":
         print("Тепло, но дождливо. Возьми зонт")
    else:
           print("Жарко! Идеально для футболки")




