# Hi I'm shayan and today I want to practice about classes
# 1. Create a class 
# 2. Use Constructer method '__init__' for adding attributes
# 3. Create methods and use attributes 
# 4. Call attributes 
# 5. Call methods

class Restaurant:
    """Represent a restaurant and its status."""
    def __init__(self, restaurant_name, cuisine_type, status):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.status = status

    def describe_restaurant(self):
        """Formatted restaurant information"""
        information = f"{self.restaurant_name.title()} is a {self.cuisine_type.upper()} restaurant"
        print(information)

    def open_restaurant(self):
        """Restaurant status"""
        restaurant_status = f"The restaurant is {self.status}"
        print(restaurant_status)

first_restaurant = Restaurant('parsian', 'persian food', 'open')

print(f"Name attribute : {first_restaurant.restaurant_name.title()}")
print(f"Cuisine type : {first_restaurant.cuisine_type.upper()}\n")
first_restaurant.describe_restaurant()
first_restaurant.open_restaurant()
