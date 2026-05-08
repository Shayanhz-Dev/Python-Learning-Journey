# Hi I'm shayan and today I want to practice getting user input
# 1. Create a list 
# 2. Create a variable and assign user input to it
# 3. Use an if-statement to check the value


car_list = ['bmw', 'subaru', 'audi', 'toyota']
car_request = input("what kind of rental car you would like?" ).lower()
if car_request in car_list:
    print("This car is available. you can rent it")
else:
    print("Sorry, we don't have this car")

