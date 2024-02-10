from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        """Calculate the person's age based on the current date."""
        today = datetime.now()
        birthdate = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    def display_details(self):
        """Display details of the person."""
        print(f"Name: {self.name}")
        print(f"Country: {self.country}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Age: {self.calculate_age()} years")

# Example usage:

person1 = Person(name="John Doe", country="USA", date_of_birth="1990-05-15")
person2 = Person(name="Alice Smith", country="Canada", date_of_birth="1985-09-21")

# Display details and age of the persons
print("Details of Person 1:")
person1.display_details()


print("\nDetails of Person 2:")
person2.display_details()

