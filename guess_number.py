# Python - Beginners
# Guess the number game between 1 & 10
# Author: jdev
# Version 0.3

from random import Random, randint, random

# Variables
num = 0
cont = 0

# Choosing difficulty
print("Hello! Welcome to Guess the number v0.3")
print("Please, choose a difficulty:")
print("\t1. Easy (1 - 10)")
print("\t2. Medium (1 - 100)")
print("\t3. Hard (1 - 1000)")
diff = input("> ")
print()

# Start the game
if int(diff) == 1:
    gnum = randint(1, 10)
    while int(num) != int(gnum):
        num = input("Guess the number: ")
        cont += 1
elif int(diff) == 2:
    gnum = randint(1, 100)
    while int(num) != int(gnum):
        num = input("Guess the number: ")
        cont += 1
elif int(diff) == 3:
    gnum = randint(1, 1000)
    while int(num) != int(gnum):
        num = input("Guess the number: ")
        cont += 1

# Win!
print(f"\nGood job! You guess the number in {cont} tries!")