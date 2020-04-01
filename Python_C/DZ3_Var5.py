import random

count = 0

n = int(input("Введите длинну списка\n"))
Spisok = []
i = 0
while i < n-1:
    a = random.randint(-20, 20)
    if a != 0:
        Spisok.append(a)
        i += 1

Spisok.append(0)

print("Список заполнен случайными значениями от -20 до 20")

for i in range(len(Spisok) - 1):
    print(Spisok[i])
    if Spisok[i] > 0 and Spisok[i+1] < 0:
        count += 1
    elif Spisok[i] < 0 and Spisok[i+1] > 0:
        count += 1
print(Spisok[n-1])
print("Знак сменился " + str(count) + " раз")