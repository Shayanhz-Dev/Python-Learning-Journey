# Hi I'm shayan and today I want to practice classes
# 1. Create class with constructor  methods and assign attributes
# 2. Create Methods and calls

class User:

    def __init__(self, f_name, l_name, age, location):

        """Represent a user's information"""

        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.location = location

    def describe_user(self):

        """Display a summary of the users information"""

        information = f"{self.f_name.title()} {self.l_name.title()} is {self.age} from {self.location}"
        print(information)

    def greet_user(self):

        """Display a greeting message"""
        
        print(f"Hello {self.f_name.title()} {self.l_name.title()} welcome!")

first_user = User('shayan', 'hasanzade', 23, 'amol')

first_user.describe_user()
first_user.greet_user()