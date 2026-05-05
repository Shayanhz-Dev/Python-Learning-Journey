#Hi I'm shayan and today I want to practice username management with lists , loops and if statement
#First I create a list with 5 value and make a for-loop for checking users to find admin
usernames = ['admin', 'jordan', 'lian', 'ada', 'sara']
for user in usernames:
    if user == 'admin':
        print(f'Hello {user.title()}, would you like to see a status report?')
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")

#Second I removed all value in list and make a if statement for find empty list 
#I create a for-loop for checking list in else statement
usernames = []
if not usernames:
    print("We need to find some users!")
else:
    for user in usernames:
        print(f"hello {user.title()}")

#Third I create two list and I want checking newe users in current_users 
#I create copy of current_users for checking all username in lowercase
#I create a for-loop for checking usernames 
current_users = ['john', 'riki', 'william', 'mina', 'jila']
new_users = ['sara', 'WILLIAM', 'MINA', 'jolia', 'tina']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry '{new_user}',that username is already taken. Please enter a new one.")
    else:
        print(f"Great! the username '{new_user}' is available.")