# Hi I'm shayan and today I want to practice about functions
# 1. Create function with 'TWO' parameters 
# 2. Print messages
# 3. Call function with 2 arguments
# Modified code :
# Multiple Function Calls

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""

    print(f"\nI have a {animal_type.upper()}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("cat", "panny")
describe_pet("dog", "raxar")

# Modified code
# Use Keyword Arguments

describe_pet(animal_type='hamster', pet_name='harry')