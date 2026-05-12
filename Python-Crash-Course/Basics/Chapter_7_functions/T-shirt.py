# Hi I'm shayan and today I want to practice functions
# 1. Create a function with parameters
# 2. Positional call
# 3. Keyword call

def make_shirt(size, text):
    """Display size T-shirt and text on the T-shirt"""
    print(f"T-shirt size is {size}")
    print(f"Text on the T-shirt is {text.upper()}")

make_shirt(48,"just do it")
make_shirt(size=49, text="be a warrior, not a worrier")

