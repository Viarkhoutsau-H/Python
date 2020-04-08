class Food:
    def eat(self):
        print("")

class Vegetables(Food):
    def eatVeg(self):
        print("I wanna eat Vegetables")

class Bread(Food):
    def eatBread(self):
        print("I wanna eat Bread")

class Meat(Food):
    def eatMeat(self):
        print("I wanna eat Meat")

class Onion(Vegetables):
    def Cut(self):
        print("I need to cut Vegetables")

class Lunch(Bread, Meat, Onion):
    def eat(self):
        print("It was a graet lunch")

food = Food()
veg = Vegetables()
bread = Bread()
meat = Meat()
on = Onion()
lunch = Lunch()

lunch.eat()
lunch.eatMeat()
food.eat()
meat.eatMeat()
on.eatVeg()
on.Cut()

