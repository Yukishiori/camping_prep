# data abstraction
import random
import math


class Food:
    # x, y, name, hp_buff,
    def __init__(self, x, y, name, hp_buff):
        self.x = x
        self.y = y
        self.name = name
        self.hp_buff = hp_buff

    def print(self):
        print("{{ {0}, {1}, {2}, {3} }}".format(self.x, self.y, self.name, self.hp_buff))


# print(Food.x)
# Init

chocolate = Food(10, 25, "chocolate", 9901)  # f => object, construct a object, f is self


# chocolate = object
# chocolate.name = "chocolate"
# chocolate.hp_buff = 9001
# chocolate.x = 10
# chocolate.y = 25


# sugar = Food(1, 2, "Sugar", 10)
# sugar.name = "sugar"
# sugar.hp_buff = 3

# print(chocolate.hp_buff)
# print(sugar.hp_buff)

# foods = [chocolate, sugar]


# java c# is close house language

# open house language :))) BAD PRACTICE THO
# chocolate.a = 10
# print(chocolate.a)

# chocolate.print()

def random_number(number):
    return math.floor(random.randrange(number))

names = ["china", "bagette", "st"]

for item in range(10):
    item = Food(random_number(100), random_number(100), names[random_number(len(names))], random_number(100))
    item.print()
