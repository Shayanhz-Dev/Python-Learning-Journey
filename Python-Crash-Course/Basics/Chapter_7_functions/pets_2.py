# Hi I'm shayan and today I want to practice functions
# I want use default values in functions
# 1. Create a function with parameters and default values
# 2. Call function with keyword argument
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""

    print(f"\nI have a {animal_type.upper()}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='willie')
