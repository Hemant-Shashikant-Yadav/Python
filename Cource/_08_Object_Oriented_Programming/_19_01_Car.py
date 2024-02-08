class Car:
    wheels = 4  # Class variable

    def __init__(self, year, model, color):
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"The {self.model} car is driving")
        print(f"The car has {self.wheels}")


    def stop(self):
        print(f"The {self.model} car is stopped")
