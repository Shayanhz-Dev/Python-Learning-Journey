# Hi I'm shyana and today I want to practice functions
# 1. Create a function with arbitrary number of arguments-parameter
# 2. Function : use for-loop for print each arguments 
# 3. Positional Call funtion
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nmaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')