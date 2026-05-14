# Hi I'm shyana and today I want to practice functions
# 1. Create a function with arbitrary number of arguments-parameter
# 2. Positional Call funtion
def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')