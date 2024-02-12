class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.year = None
        self.color = None

    def add_values(self, year, color):
        self.year = year
        self.color = color

    def drive(self):
        print(f"This {self.make} is driving")

    def stop(self):
        print("This car has stopped")

    def get_car_data(self):
        return (f"Brand {self.make}\n"
                f"Model {self.model}\n"
                f"Year  {self.year}\n"
                f"Color {self.color}\n"
                )
