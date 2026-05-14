# Hi I'm shyana and today I want to practice functions
# 1. Create a function with an arbitrary number of arguments
# 2. Function: use a for-loop to print each argument 
# 3. Positional function calls
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings.")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')