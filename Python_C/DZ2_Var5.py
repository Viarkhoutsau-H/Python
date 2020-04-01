x = -1
k = 6
y = 1.6 * (10 ** -4)

print("-------FOR--------")
A = [0.9, 8.4, 2]
for i in range(len(A)):
    c = A[i] * k - (y ** -2)/0.4
    d = 2.73 ** (1 - 2.73) + 4.9 * (x ** 2 + 1)
    print(str(i+1) + ") c = " + str(c) + "; d = " + str(d))

print("-------WHILE--------")
i = 0
while i <= 3:
    c = i * k - (y ** -2) / 0.4
    d = 2.73 ** (1 - 2.73) + 4.9 * (x ** 2 + 1)
    print(str(i) + ") c = " + str(c) + "; d = " + str(d))
    i += 0.5

print("-------Double--------")
A = [0.9, 8.4, 2]
Y = [1.3, -8, 0.2]
x = 1
while x <= 2:
    for i in range(len(A)):
        c = A[i] * k - (Y[i] ** -2) / 0.4
        d = 2.73 ** (1 - 2.73) + 4.9 * (x ** 2 + 1)
        print(str(x) + ") c = " + str(c) + "; d = " + str(d))
    x += 0.1
