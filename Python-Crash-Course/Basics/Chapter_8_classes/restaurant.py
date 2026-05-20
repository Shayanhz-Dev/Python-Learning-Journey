# Hi I'm shayan and today I want to practice about classes
# 1. Create a class 
# 2. Use Constructer method '__init__' for adding attributes
# 3. Create methods and use attributes 
# 4. Call attributes 
# 5. Call methods
# 6. Create a child class with parent attributes and special attributes
# 7. Create methods for child class
# 8. Call methods 

class Restaurant:
    """Represent a restaurant and its status."""
    def __init__(self, restaurant_name, cuisine_type, status):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.status = status

    def describe_restaurant(self):
        """Display a summary of the restaurant's information."""
        information = f"{self.restaurant_name.title()} is a {self.cuisine_type.upper()} restaurant"
        print(information)

    def open_restaurant(self):
        """Restaurant status"""
        restaurant_status = f"The restaurant is {self.status}"
        print(restaurant_status)

class IceCreamStand(Restaurant):
    """A Icecreamstand for free space in restaurant"""

    def __init__(self, restaurant_name, cuisine_type, status):
        """Initialize attributes to describe a Icecreamstands."""
        super().__init__(restaurant_name, cuisine_type, status)
        
        self.flavors = ['apple', 'orange', 'banana']

    def show_flavors(self):
        """Display flavors lists"""

        print("\nflavors list in menu:")
        for flavor in self.flavors:
             print(f"- {flavor.title()}")

restaurant = Restaurant('parsian', 'persian food', 'open')
icecreamstand = IceCreamStand('parsian', 'icecream', 'close')

print(f"Name attribute : {restaurant.restaurant_name.title()}")
print(f"Cuisine type : {restaurant.cuisine_type.upper()}\n")
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"Name attribute : {icecreamstand.restaurant_name.title()}")
print(f"Cuisine type : {icecreamstand.cuisine_type.upper()}\n")
icecreamstand.describe_restaurant()
icecreamstand.open_restaurant()
icecreamstand.show_flavors()
