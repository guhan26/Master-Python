
# Creating function
def my_method():
    print("hii guhan")
# Calling the function
my_method()

# Creating Class and class name my_functionone
class MyClass:
    def my_functionone(self):
        print("Hello World")
    def my_functiontwo(self):
        print("my function is calling")
# creating object
obj = MyClass()

# calling function using object
obj.my_functionone()
obj.my_functiontwo()

class laptop:
# __init__() function constructor
    def __init__(self):
        print("demo")
        self.brand = "Lenova"
# class is using the self keyworld to refer the object
    def methodtwo(self):
        self.brand = "HP"
        print("ram",self.ram)
        print("processor",self.processor)

hp = laptop()
hp.ram="6gb"
hp.processor="i5"

hp.ram="5gb"
hp.processor="i6"
# self is call current values
hp.methodtwo()

# Inheritance

#Single inheritance
class dad():
    def phone(self):
        print("dad's phone")
class son(dad):
    def laptop(self):
        print("son's phone")

obj1 = son()
obj1.laptop()
obj1.phone()

# Multiple Inheritance
class Dad(object):

    @staticmethod
    def phone(self) -> None:
        print("dad's phone")
class Mom(object):
    def phonetwo(self):
        print("mom's phone")
class Son(Dad, Mom):
    def laptop(self):
        print("son's phone")

obj1 = son()
obj1.laptop()
obj1.phonetwo()
obj1.phone()

# Multi-level Inheritance
class dad():
    def phone(self):
        print("dad's phone")
class mom(dad):
    def phonetwo(self):
        print("mom's phone")
class son(mom):
    def laptop(self):
        print("son's phone")

obj1 = son()
obj1.laptop()
obj1.phonetwo()
obj1.phone()

# Hierarchical Inheritance -- Two childs inherit one parent
# Hybrid Inheritance -- It allows all Inheritance

# polymorphism

class A():

    def add1(self):
        print("i am guhan")

class B(A):
    def add1(self):
        print("i am not a guhan")

over = B()
over.add1()



