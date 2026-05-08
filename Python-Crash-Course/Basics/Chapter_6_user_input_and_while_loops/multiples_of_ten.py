# Hi I'm shayan and today I want to practice input getting user values
# 1. Create a variable and assign in user values
# 2. If-statement to checking user value is digit or not
# 3. Change string user-value to a numrical value
# 4. If-statement checking user-value 

user_number = input("Please, Enter a number: ")
if user_number.isdigit():
    user_number = int(user_number)
    if user_number % 10 == 0:
        print(f"Your number {user_number} is a multiple of 10")
    else:
        print(f"Your number {user_number} is a not multiple of 10")
else:
    print("Please, Enter a valid number")