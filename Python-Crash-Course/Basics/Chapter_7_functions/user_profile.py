# Hi I'm shayan and today I want to practice function
# 1. Create a function with positional parameters and arbitrary keyword arguments
# 2. Add positional arguments to the dictionary
# 3. Return the generated dictionary containing user information
# 4. Call the function and assign the result to a variable

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='phtsics')
my_profile = build_profile('shayan', 'hasanzade',
                           location= 'amol',
                           field= 'sadaf',
                           age= 23)
print(user_profile)
print(my_profile)