# Hi I'm shayan and today I want to practice function
# 1. Create function with names parameters
# 2. Use for-loop for use every argument assign in parameters
# 3. Create a list 
# 4. Positional Call with list argument


def greet_users(names):
    """print a simple greeting to each user in the list."""
    for name in names:
        msg = f"hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)