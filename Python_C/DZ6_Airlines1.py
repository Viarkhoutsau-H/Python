class Plane:

    __number = 0

    def __init__(self, number, city, weekDay):
        self.number = number
        self.city = city
        self.weekDay = weekDay
        print("Был создан самолет с номером рейса - " + str(number))


    def __del__(self):
        print("")

    def __setattr__(self, key, value):
        if key == 'number' or key == 'city' or key == 'weekDay':
            self.__dict__[key] = value
        else:
            raise AttributeError

    def __str__(self):
        return str(self.number) + " " + str(self.city) + " " + str(self.weekDay)

    def setNumber(self, number):
        self.__number = number

    def getNumber(self):
        return self.number

    def getCity(self):
        return self.city

    def getWeekDay(self):
        return self.weekDay

class AirLines:
    def __init__(self):
        self.City = []
        self.WeekDay = []

    def __str__(self):
        return str(self.City) + "\n" + str(self.WeekDay)

    def addPlane(self, number, city, weekDay):
        plane = Plane(number, city, weekDay)
        if city == 'Minsk' and weekDay == 'Monday':
            self.City.append(plane.number)
            self.WeekDay.append(plane.number)
        elif weekDay == 'Monday':
            self.WeekDay.append(plane.number)
        elif city == 'Minsk':
            self.City.append(plane.number)
        else:
            print("Объект с номерам рейса " + str(plane.number) + " не был создан")
            print("Хрен тебе")

    def getCity(self):
        print("Список с пунктами назначения - ")
        for i in range(len(self.City)):
            print(self.City[i])

    def getWeekDay(self):
        print("Список с днями вылетов - ")
        for i in range(len(self.WeekDay)):
            print(self.WeekDay[i])

airLines = AirLines()
airLines.addPlane(1, 'Minsk', 'Monday')
airLines.addPlane(2, 'Moscow', 'Monday')
airLines.addPlane(3, 'Minsk', 'Friday')
airLines.addPlane(4, 'London', 'Sunday')


print(airLines.getCity())
print(airLines.getWeekDay())