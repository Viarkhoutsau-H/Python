import random


n = int(input("Введите длинну списка\n"))
Spisok = []

for i in range(n):
    a = random.randint(0, 99)
    print(a)
    Spisok.append(a)

for i in range(len(Spisok)):
    if i % 7 == 0 and i != 0:
        Spisok.pop(i)

print("Длинна списка после удаления - " + str(len(Spisok)))
for i in range(len(Spisok)):
    print(Spisok[i])