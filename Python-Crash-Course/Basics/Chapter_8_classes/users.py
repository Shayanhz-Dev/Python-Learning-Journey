# Hi I'm shayan and today I want to practice classes
# 1. Create class with constructor  methods and assign attributes
# 2. Create Methods and calls

class User:

    def __init__(self, f_name, l_name, age, location, login_attempts=0):
        """Represent a user's information"""

        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.location = location
        self.login_attempts = login_attempts

    def describe_user(self):
        """Display a summary of the user's information"""

        information = f"{self.f_name.title()} {self.l_name.title()} is {self.age} from {self.location}"
        print(information)

    def greet_user(self):
        """Display a greeting message"""
        
        print(f"Hello {self.f_name.title()} {self.l_name.title()} welcome!")

    def increment_login_attempts(self):
        """Counting login attempts"""

        self.login_attempts += 1 
        print(f"New login attempts {self.login_attempts}")

    def reset_login_attempts(self):
        """Reset user login attempts"""
        
        self.login_attempts = 0
        print(f"Login attempts reset, now is {self.login_attempts}")

first_user = User('shayan', 'hasanzade', 23, 'amol', 4)
first_user.increment_login_attempts()
first_user.reset_login_attempts()
first_user.describe_user()
first_user.greet_user()