# Test 000 Python - Beginners
# Guess the number game between 1 & 10
# Author: jdev

from random import Random, randint, random

# Variables
a = randint(1, 10)
num = 0
cont = 0

while int(num) != int(a):
    num = input("Guess the number: ")
    cont = cont + 1

print(f"Good job! You guess the number in {cont} tries!")