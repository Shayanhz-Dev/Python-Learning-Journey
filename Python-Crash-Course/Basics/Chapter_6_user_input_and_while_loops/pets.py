# Hi I'm shayan and today I want to practice input getting user and while-loop
# 1. Create a list and print
# 2. Use while-loop for 'cat' values in list and remove all 'cat' value
# 3. Print the updated list.


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)