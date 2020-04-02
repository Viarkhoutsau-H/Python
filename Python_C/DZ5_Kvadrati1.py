def Recursia(a, b, c = 1):
    minimum = min(a, b)
    maximum = max(a, b)
    S = a * b
    if maximum % c == 0 and minimum % c == 0:
        count = S / (c ** 2)
        if count == 1:
            print("В прямоугольник помещается " + str(int(count)) + " квадрат площадью " + str(
                c ** 2) + " и сторонами " + str(c))
        else:
            print("В прямоугольник помещаются " + str(int(count)) + " квадратов площадью " + str(
                c ** 2) + " и сторонами " + str(c))
        c += 1
        return Recursia(a, b, c)
    elif c <= minimum:
        c += 1
        return Recursia(a, b, c)
    else:
        print("На этом всё")


a = int(input("Введите А - \n"))
b = int(input("Введите B - \n"))
Recursia(a,b)