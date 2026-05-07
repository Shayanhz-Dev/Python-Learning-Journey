# Hello I'm shayan and today I want to practice how use list in a dictionary
# 1. create a dictionary with key-value
# 2. assign a list like value 
# 3. create for-loop for print each item list-value in pizza dictionary
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese'],
}
# Summarize the order

print(f"you ordered a {pizza['crust']}-crust pizza"
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")