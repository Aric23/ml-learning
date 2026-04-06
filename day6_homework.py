chisla = [1, 2, 4, 6, 2, 4, 5, 6, 8, 8]
chisla1 = []
print(chisla)
for chi in chisla:
    if chi in chisla1:
        print("Это число уже существует")
    else:
        
        chisla1.append(chi)
        print(f"такое число еще нету в chisla1")
        print(chisla1)
    
print(chisla)
print(sorted(chisla1))

chisla3 = [1, 2, 4, 6, 2, 4, 5, 6, 8, 8]
chisla4 = []
chisla5 = []
 
for ch in chisla3:
    if ch % 2 == 0:
        chisla4.append(ch)
    else:
        chisla5.append(ch)


print("Четные - ", chisla4)
print("Нечетные - ", chisla5)

a = [1, 2, 3]
b = ["a", "b", "c"]
result = []

for i in range (len(a)):
    result.append(a[i])
    result.append(b[i])


print(result)


txt = input("Введите предложение - ")
txt_list = txt.split()
print("Количество слов - ", len(txt_list))
most = ""
for word in txt_list:
    if len(most) < len(word):
        most = word
    else:
        continue

print("Самое длиное слово - ", most)
txt_list.reverse()
print("в обратном порядке - ", txt_list)
    