# when the object is taken as argument the classtype is not checked by python
# if the mentioned attributes are inside the object then it is meant valid

class Duck:

    def walk(self):
        print("Duck is walking")
    
    def talk(self):
        print("Duck is quacking")

class NotDuck:

    def walk(self):
        print("It can't walk")
    
    def talk(self):
        print("It can't talk")

def global_function(something):
    something.walk()
    something.talk()

duck_1 = Duck()

chair = NotDuck()

global_function(duck_1)
global_function(chair)