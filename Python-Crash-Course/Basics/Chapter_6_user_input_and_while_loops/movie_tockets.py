# Hi I'm shayan and today I want to practice input getting users and while loops
# 1. Create prompt message
# 2. Create while-true-loop
# 3. Make variable for user input prompt with .strip() .lower() for getting clean input
# 4. Use if statement for checking 'quit' to end the program
# 5. Elif for rest program for empty input
# 6. Elif change string to numrical
# 7. make if-statements numrical  
# 8. Else statement for unnumrical inputs

prompt = "\nPlease, Enter your age for buy ticket: "
prompt += "\n(Enter 'quit' to end the program) "

while True:
    age_input = input(prompt).strip().lower()
    if age_input == 'quit':
        break
    elif age_input == "":
        continue
    elif age_input.isdigit():
        age = int(age_input)

        if age <= 3:
            print(f"✅ You are {age} years old, ticket is free")
        elif 3 < age <= 12:
            print(F"✅ You are {age} years old, your ticked cost is $10")
        else:
            print(f"✅ You are {age} years old, your ticket cost is $15")
    else:
        print("⚠️ Please enter a valid number for your age.")


