def count_lines(filename):
    n = 0
    with open(filename, "r", encoding="utf-8") as f:
        for i in f:
            n += 1
    
    print(n)

count_lines("todo.txt")

def find_word(filename, word):
    lists = []
    with open(filename, "r", encoding="utf-8") as f:
        for i, fr in enumerate(f, 1):
            if word in fr:
                lists.append(i)
    
    print(lists)

find_word("todo.txt", "молоко")

def merge_files(file1, file2, output):
     with open(file1, "r", encoding="utf-8") as f:
        file1r = f.read()
    
     with open(file2, "r", encoding="utf-8") as f:
        file2r = f.read()
     
     with open(output, "w", encoding="utf-8") as f:
        f.write(file1r)
        f.write(file2r)

     print("Успешно")

merge_files("todo.txt", "todo_backup.txt", "ottt.txt" )
while False:
    try:
        a = int(input("Введите первое число "))
    except ValueError:
        print("Ошибка: нужно ввести число!")
        return False
    else:
        return True

try:
    b = int(input("Введите второе число "))
except ValueError:
    print("Ошибка: нужно ввести число!")

c = input("Введите опирацию - (+,-,*,/) ")

try:
    if c =="+":
        print(f"{a} +{b} = {a+b}")
    elif c =="-":
        print(f"{a} -{b} = {a-b}")
    elif c =="*":
        print(f"{a} *{b} = {a*b}")
    elif c =="/":
        print(f"{a} /{b} = {a /b}")
except ValueError:
    print("Ошибка: нужно ввести число!")
except ZeroDivisionError:
    # Ошибка деления на ноль
    print("Ошибка: деление на ноль!")





    
       
