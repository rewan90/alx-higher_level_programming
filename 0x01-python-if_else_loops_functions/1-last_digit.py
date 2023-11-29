#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nom = abs(number) % 10
if number < 0:
    nom = -nom
print(f"Last digit of {number:d} is {nom:d} and is ", end="")
if nom > 5:
    print("greater than 5")
elif nom == 0:
    print("0")
else:
    print("less than 6 and not 0")