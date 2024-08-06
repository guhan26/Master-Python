# class and object
class Vehicle:
    # this is class attribute
    vehicle_counter = 0
# __init__ is the constructor method
    def __init__(self, body_type, make):
        # Instance attributes
        self.vehicle_body = body_type
        self.vehicle_make = make
        Vehicle.vehicle_counter += 1

    def get_vehcile_count(self):
        # Accessing class attribute
        return Vehicle.vehicle_counter


    def drive(self):
        # Accessing instance attributes
        print("Vehcile Driving...")

# Inheritance and Polymorphism
class Guhan(Vehicle):
    def drive(self):
        print("Truck Driving...")


class GoodGuhan(Vehicle):
        def drive(self):
            print("Motorcycle Driving...")
          
