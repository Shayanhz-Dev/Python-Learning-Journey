# Hi I'm shayan and today I want to practice input getting user values
# 1. Create a variable and assign input user value
# 2. If-statement to checking user value is digit or not
# 3. If-statement to checking user value 


dinner_group = input("How many people are in your dinner group? ")

if dinner_group.isdigit():
    number = int(dinner_group)
    if number > 8:
        print("\nYou have to wait for a table.")
    else: 
        print("\nYour table is ready.")
else:
    print("Please enter a number.")