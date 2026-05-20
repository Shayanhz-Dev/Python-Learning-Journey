# Hi I'm shayan and today I want to practice random library
# Create a random lottery pool and analysis lottery

import random

lottery_pool = [1, 3, 13, 12, 4, 5, 78, 66, 99, 32, 'A', 'B', 'C', 'D', 'G', 44, 33, 94, 11, 14]
my_ticket = "G"
attempts = 0

while True:
    attempts += 1
    win_ticket = random.sample(lottery_pool, 4)

    if my_ticket in win_ticket:
        print(f"You win! {win_ticket}")
        print(f"{attempts} try for winning")
        break
    else:
        if attempts % 5 == 0:
            print(f"{attempts} try , you dont win")

