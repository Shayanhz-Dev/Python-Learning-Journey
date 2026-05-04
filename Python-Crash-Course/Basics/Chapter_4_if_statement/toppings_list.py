#Hi I'm Shayan and today i want to practice if statement 
#I want to know how works "elife"
requested_toppings = ['extra cheese','green peppers','mushrooms']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print("\nFinished making your pizza!")

#Modify code becuase i want to practice today checking for special item

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")
