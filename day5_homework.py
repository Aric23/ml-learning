a = int(input(" N - "))
c = 0
for i in range(2, a+1, 2):
    c=c+i

print(f"Sum - {c}")


N = int(input(" N - "))
for i in range(N, 1, -1):
    print(i)

print("Пуск")


B = int(input(" N - "))
for i in range(1, B+1):
    if B% i == 0:
        print(i)
    else:
        continue


G = int(input(" N - "))

for i in range(1, G+1):
    if (2**i) < G:
        print(2**i)
    else: 
        continue