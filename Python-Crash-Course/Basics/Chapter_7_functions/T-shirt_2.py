# Hi I'm shayan and today I want to practice functions
# 1. Create a function with parameters and default values
# 2. Positional call
# 3. Keyword call

def make_shirt(text, size="Large"):
    """Display size T-shirt and text on the T-shirt"""
    print(f"T-shirt size is {size}")
    print(f"Text on the T-shirt is {text.upper()}")

make_shirt("just do it")
make_shirt(text="be a warrior, not a worrier")

