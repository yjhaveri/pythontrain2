#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#
class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginestyle):
        super().__init__("Car")
        self.enginestyle = enginestyle
        self.doors = 4
        self.wheels = 4
    
    def drive(self, speed):
        super().drive(speed)


class Motorcycle(Vehicle):
    def __init__(self, enginestyle, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginestyle = enginestyle

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

print(mc1.wheels)
print(car1.doors)
print(car2.enginestyle)
