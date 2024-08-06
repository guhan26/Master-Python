"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""

# Assignment 1

class Animal:
    def __init__(self):
        print("Animal Constructed")

    def move(self):
        print("Animal Moving...")

    def eat(self):
        print("Animal Eating...")

class Dog(Animal):
    def __init__(self, brid_age, brid_name):
        Animal.__init__(self)
        self.age = brid_age
        self.name = brid_name

    def move(self):
        print("Fish flying...")

mydog = Dog(3,"wabcd")
mydog.move()
mydog.eat()

# output:- 
#     Animal Constructed
#     Fish flying...
#     Animal Eating...
