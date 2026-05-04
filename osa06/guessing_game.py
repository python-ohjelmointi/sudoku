"""
Guessing game for demonstrating the prompts.py file
"""

from random import randint
from prompts import ask_number

correct = randint(0, 100)
answer = -1

while answer != correct:
    answer = ask_number("Guess my number: ", 0, 100)

    if answer < correct:
        print("Too low!")
    if answer > correct:
        print("Too high!")


print("Done! Nice job!")
