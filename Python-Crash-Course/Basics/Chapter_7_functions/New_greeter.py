# Hi I'm shayan and today I want to practice function and return values
# 1. Create function with parameters 
# 2. Create a variable for formatted name
# 3. Return variable 

def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Modified code:
# This is an infinite loop!
# 1. Create infinite while-loop
# 2. getting input values 
# 3. Call function with variable and input values arguments
while True:
    print("\nPlease tell me your name")
    f_name = input("First Name: ").strip().lower()
    l_name = input("Last Name: ").strip().lower()

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")