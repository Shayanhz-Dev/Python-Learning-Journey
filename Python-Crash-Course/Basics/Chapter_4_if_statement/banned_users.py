#Hi I'm Shayan and I want to practice if statement with list and find value is not in a list!
#First of all I create a list and variable with value
#Second I create one if statement with (not in) for list and print a message 

banned_user = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_user:
    print(f"{user.title()}, you can post a response if you wish.")