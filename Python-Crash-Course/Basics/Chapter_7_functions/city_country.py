# Hi I'm shayan and today I want to practice function
# 1. Create function
# 2. Create variable 
# 3. Return Variable
# 4. Positional Calls function

def city_country(city, country):
    formatted = f"{city}, {country}"
    return formatted.title()
print(city_country('amol', 'iran'))
print(city_country('berlin', 'germany'))
print(city_country('New yurk', 'united states'))