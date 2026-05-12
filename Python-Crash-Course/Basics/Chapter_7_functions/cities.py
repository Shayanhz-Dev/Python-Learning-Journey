# Hi I'm shayan and today I want to practice functions
# 1. Create a function with parameters and default values
# 2. Call function with positional argument and keyword arguments

def describe_city(city, country='iran'):
    """Display city in country"""
    print(f"{city.title()} is in {country.title()}")
describe_city('amol')
describe_city(city='tehran')
describe_city(country="germany", city='munich')