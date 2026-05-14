# Hi I'm shayan and today I want to practice function
# 1. Create a function with *args
# 2. Use for-loops to print each item
# 3. Positional Call function


def sandwich_toppings(*toppings):
    """Display sandwich toppings"""
    print(f"\n-------------------")
    print("Your sandwich toppings order:")
    print("\n(Started adding toppings.....)")
    for topping in toppings:
        print(f"- {topping.upper()} added.")

sandwich_toppings('extra cheese', 'mushrooms', 'potato')
sandwich_toppings('chicken','mushrooms')
