# Hi I'm shayan and today I want to practice input user value 
# 1. Create Variable with input
# 2. Change string to numrical with 'int' 
# 3. use if statement to checking user have standard height for rollercoaster


height = input("how tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")