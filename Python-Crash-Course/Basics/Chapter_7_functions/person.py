# Hi I'm shayan and today I want to practice functions
# Return a dictionary 
# 1. Create a function with parameters
# 2. Create a dictionary with key-parameters- 
# 3. Return 
# 4. Create a variable to Call function with arguments (there is argument is values of the dictionary keys)


def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)