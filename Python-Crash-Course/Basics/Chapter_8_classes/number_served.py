# Hi I'm shayan and today I want to practice about classes
# 1. Create a class 
# 2. Use Constructer method '__init__' for adding attributes
# 3. Create methods and use attributes 
# 4. Call attributes 
# 5. Call methods
# This is modified restaurant.py 
# 6. Create method for served number
# 7. Create method for additional served number

class Restaurant:
    """Represent a restaurant and its status."""
    def __init__(self, restaurant_name, cuisine_type, status):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.status = status
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant's information."""
        information = f"{self.restaurant_name.title()} is a {self.cuisine_type.upper()} restaurant"
        print(information)

    def open_restaurant(self):
        """Restaurant status"""
        restaurant_status = f"The restaurant is {self.status}"
        print(restaurant_status)

    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't roll back the number of served customers!")

    def increment_number_served(self, additional_customers):
        """Add the given amount to the number of customers served."""
        if additional_customers >= 0:
            self.number_served += additional_customers 
        else:
            print("You can't add negative customers!")


restaurant = Restaurant('parsian', 'persian food', 'open')

print(f"initial number served {restaurant.number_served}")
restaurant.number_served = 15
print(f"report updated number served {restaurant.number_served}")

restaurant.set_number_served(45)
print(f"\nNew Number served a new day {restaurant.number_served}")

restaurant.increment_number_served(15)
print(f"Number served after 12h today {restaurant.number_served}")

print(f"Name attribute : {restaurant.restaurant_name.title()}")
print(f"Cuisine type : {restaurant.cuisine_type.upper()}\n")
restaurant.describe_restaurant()
restaurant.open_restaurant()
