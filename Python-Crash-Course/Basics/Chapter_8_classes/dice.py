# Hi I'm shayan and today I want to practice classes
# 1. Create a class with attributes and methods
# 2. import random library and use randint for my method
# 3. Create dices with positional call class 
# 4. use for-loop for create a many rolling

from random import randint

class Die:
    """Create a Dice and random roll"""
    def __init__(self, sides=6):
        """Represent a dice and its sides."""

        self.sides = sides

    def roll_die(self):
        """Create a random rolling"""

        return randint(1, self.sides)

my_die = Die()
print("--- 6-side die ---")
for _ in range(10):
    print(my_die.roll_die())

print("\n--- 10-side die ---")
die_10 = Die(10)
for _ in range(10):
    print(die_10.roll_die())

print("\n--- 20-side die ---")
die_20 = Die(20)
for _ in range(10):
    print(die_20.roll_die())