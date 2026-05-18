# Hi I'm shayan and today I want to practice about classes
# 1. Create a Class
# 2. Create a method for construction class attribute 
# 3. Create a method for make a formatted name
# 4. Create a method for odometer 

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")    
    
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40
    
    def describe_battery(self):
        """Print a statement describing the battrey size."""
        print(f"This car has a {self.battery_size}-kwh battery size.")

    def fill_gas_tank(self):
        """Electric cars dont have gas tanks."""
        print("this car doesn't have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.fill_gas_tank()