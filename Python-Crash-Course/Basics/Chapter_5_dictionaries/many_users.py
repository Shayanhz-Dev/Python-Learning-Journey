# A dictionary in dictionary 
# Hi I'm shayan and I want to practice today about nesting
# 1. Creatث one dictionary and create new dictionary in the first dictionary
# 2. Assign value in First and my value is second dictionary
# 3. Assign value in second dictionary
# 4. For-loop for with item() method to checking and return value in my dictionaries 
# 5. Create variable and I assign dictionary items in this
# 6. Print variable

users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")