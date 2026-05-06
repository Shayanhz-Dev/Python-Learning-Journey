# Hi I'm shayan and today I want to practice dictionary 
# First , I create a dictionary with key-value
# I create for-loop for my dictionary 
# I use .item() method for return key-value to me
# I print name,numbers key-value

favorite_numbers = {'mehdi': 6, 'mozhgan':5, 'sarina':9, 'shayan': 7}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {numbers}")