# Double under methods
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + "age is "+ str(self.age)

    def __len__(self):
        return self.age

tom = Employee("tom",47)

print(tom)

mylist = [2,3,4,6]

print(len(tom))
