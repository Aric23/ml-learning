def is_prime(n):
    total = 0
    if n > 1:
        for i in range(2, n):
            if n % i > 0:
                continue
            else:
                total += 1
                
    if total == 0:
        return "Простое"
    elif total > 0:
        return "НЕ простое"
    else:
        return "Меньше 1"


a = 4
print(f"Число {a} - {is_prime(a)}")

def factorial(n):
    res = 1
    for i in range(2, n+1):
        res = res * i

    return res


print(f"Факториал 5 - {factorial(5)}")

def reverse_string(s):
    s.reverse()
    return s 

print(f"Список в обратке - {reverse_string([1, 2 , 3, 4, 5])}")


def count_vowels(s):
    b = s.strip().lower()
    print(b)
    ch = 0
    glas = set("aeiouyаоуиэы")
    for char in b:
        if char in glas:
            
            ch +=1
        else:
            continue
    
    return ch
p = "ааааааааааааааа"
print(f"Количество гласных в {p},  {count_vowels(p)}")

