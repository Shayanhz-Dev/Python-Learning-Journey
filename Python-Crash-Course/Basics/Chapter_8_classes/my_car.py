# Hi i'm shayan and today I want to practice import classes in program
# from (file_name) import (class_name)
from car_class import Car

my_new_car = Car('audi', 'a4', '2024')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()