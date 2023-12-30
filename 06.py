class Vehicle:
    # Class attribute with a default value
    color = "white"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}")

# Example usage:
vehicle1 = Vehicle(make="Toyota", model="Camry", year=2022)
vehicle2 = Vehicle(make="Honda", model="Civic", year=2023)

# Display details of vehicles
vehicle1.display_details()
vehicle2.display_details()