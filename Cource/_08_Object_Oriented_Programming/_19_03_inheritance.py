class Animal:
    isalive = True

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Lion(Animal):

    def run(self):
        print(f"{self.name} is running")


class Hawk(Animal):
    def fly(self):
        print(f"{self.name} is flying")


ryan = Lion("ryan")
ryan.run()
ryan.sleep()

homelander = Hawk("john")
homelander.fly()
