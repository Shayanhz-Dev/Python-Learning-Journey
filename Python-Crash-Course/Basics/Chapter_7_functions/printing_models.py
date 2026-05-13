# Hi I'm shayan and today I want to practice function
# 1. Create lists with values and empty
# 2. Use while-loop
# 3. Popping first list items
# 4. Append first list items to second list
# 5. Use for-loop for print second list items

# start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate Printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"printing model : {current_design}")
    completed_models.append(current_design)
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)