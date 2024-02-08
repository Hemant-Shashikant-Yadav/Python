class Car:
    def turn_on(self):
        print("car turned on")
        return self

    def drive(self):
        print("Drive")

    def brake(self):
        print("Brake")

    def turn_off(self):
        print("car turned off")


car = Car()

car.turn_on().drive()
