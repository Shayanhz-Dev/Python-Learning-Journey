# Hi I'm shayan and today I want to practice input getting user and while loop
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
# 1. We create two lists: the first list has values and the second list is empty.
# 2. Use a while-loop to extract values from the first list using pop().
# 3. Print a message for each value and append it to the second list.
# 4. Use for-loop to show second list values and report
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user  until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
