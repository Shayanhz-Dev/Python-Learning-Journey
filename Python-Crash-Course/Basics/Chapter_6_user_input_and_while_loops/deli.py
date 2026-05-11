# Hi I'm shayan and today I want to practice about lists and while loop
# 1. Create list with values and empty list
# 2. Use while loop on list
# 3. Poping list values and assign in new variable
# 4. Appending poping items to empty list
# 5. Use for-loop for print message 


sandwich_order = ['Hamburger', 'Cheeseburger', 'Chicken', 'Roast Beef']
finished_sandwich = []

while sandwich_order:
    current_sandwich = sandwich_order.pop(0)
    print(f"I made your {current_sandwich} sandwich")
    finished_sandwich.append(current_sandwich)
print("\n--- all sandwiches made ---")
for sandwich in finished_sandwich:
    print(f"-{sandwich.title()} sandwich")
