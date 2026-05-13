# Hi I'm shayan and today I want to practice function
# This is function version printing_models.py 
# 1. Create a function 
# 3. Popping first list items
# 4. Append first list items to second list
# 5. Create second function
# 6. Use for-loop for print second list items
# 7. Positional call first function with two list-argument
# 8. Positional call second function with second list-argument

# Start with some designs that need to be printed
def print_models(unprinted_designs, completed_models):

    """Simulate Printing each design, until none are left.
    Move each design to completed_models after printing."""

    while unprinted_designs:
         current_design = unprinted_designs.pop()
         print(f"printing model : {current_design}")
         completed_models.append(current_design)

def show_completed_models(completed_models):

    """Display all completed models"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)