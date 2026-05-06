# Practicing Python dictionaries
# 1. Create a dictionary with key-value pairs
# 2. Loop through it using .items()
# 3. Print each name and its favorite number


favorite_numbers = {
    'mehdi': 6, 
    'mozhgan': 5,
    'sarina': 9,
    'shayan': 7,
                    }
for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}")