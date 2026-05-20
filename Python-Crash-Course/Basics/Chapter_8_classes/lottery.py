# Hi I'm shayan and today I want to practice random library
# Create a random lottery pool and report winning tickets 

import random

lottery_pool = [1, 3, 13, 12, 4, 5, 32, 66, 99, 32, 'A', 'B', 'C', 'D', 'G']
winning_tickets = random.sample(lottery_pool, 4)

print(winning_tickets)
