import random



while 1:
    month = int(input("Введите номер месяца\n"))
    if 1 <= month < 3 or month == 12:
        print("Сейчас зима!")
        break
    elif 3 <= month < 6:
        print("Сейчас весна!")
        break
    elif 6 <= month < 9:
        print("Сейчас лето!")
        break
    elif 9 <= month < 12:
        print("Сейчас осень")
        break
    else:
        print("Номер месяца не подходитБ попробуйте снова!")