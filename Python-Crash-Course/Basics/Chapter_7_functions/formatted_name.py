# Hi I'm shayan and today I want to practice function and return values
# This is my first return values
# 1. Create function with parameters 
# 2. Create a variable for formatted name
# 3. Return variable 
# 4. Create a variable and assign call+arguments

def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)