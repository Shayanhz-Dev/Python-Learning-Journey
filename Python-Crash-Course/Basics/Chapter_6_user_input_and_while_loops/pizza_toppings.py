# Hi I'm shayan and today I want to practice input getting user and while-loops
# 1. Create prompt and messages
# 2. Create empty list
# 3. Create while True loop
# 4. Create variable input with strip() lower() methods for getting clean input orders
# 5. If-statement 'quit' for break loop and end program
# 6. Elif-statement for empty input
# 7. Else-statement for real topping input
# 8. If-statement for exist value on list and print the toppings list
# 9. Else-statement for reporting list is empty


prompt = "\nPlease select your pizza topping:"
prompt += "\n(Enter 'quit' to end the program.)\n"

toppings = []

while True:
    topping = input(prompt).strip().lower()
    if topping == 'quit':
        break
    elif topping == '':
        print("⚠️ You didn't enter anything! Please type a topping.")
        continue
    else:
        toppings.append(topping)
        print(f"✅ Your topping '{topping}' was added!")

if toppings:
    print("\n🍕 Final list of your toppings:")
    for topping_pizza in toppings:
        print(f" - {topping_pizza.title()}")
else:
    print("\nNo toppings selected.")
