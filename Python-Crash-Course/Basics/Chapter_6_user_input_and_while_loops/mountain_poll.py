# Hi I'm shayan and today I want to practice input getting user and while-loops
# 1. Create a empty dictionary
# 2. Create a True flag
# 3. Use while-loops and input values
# 4. Add key-value (name = key , value = response)
# 5. Input value
# 6. Use if statement for asking repeat the program or exit.
# 7. Use For-loops for items in the dictionary and print it


responses = {}
# Set a flag to inddicate that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ").lower().strip()
    response = input("Which mountain would you like to climb someday? ").lower().strip()

    # Store the response in the dictionary
    responses[name] = response 

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ").lower().strip()
    if repeat == "no":
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")
