#Hi I'm shayan and I want to practice to day if statement + elife

age = 12
if age < 4:
    print("your admission cost is $0.")
elif age < 18:
    print("your admission cost is $25.")
else:
    print("your admission cost is $40.")

#We can create a variable in each if statements

if age < 4 :
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"\nYour admission cost is ${price}.")

#I want using Multiple elif Blocks and modify last codes

if age < 4 :
    price = 0
elif age < 18:
    price = 25
elif age < 40:
    price = 40
else:
    price = 20
print(f"\nYour admission cost is ${price}.")

#Omitting the else Block

if age < 4 :
    price = 0
elif age < 18:
    price = 25
elif age < 40:
    price = 40
elif age >= 65:
    price = 20
print(f"\nYour admission cost is ${price}.")