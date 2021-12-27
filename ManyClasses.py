class Rectangle:
    def AreaOfIt (self):
        return self.length * self.width

    def __init__(self,width,length):
        self.width = width
        self.length = length


a = Rectangle(5, 10)
print(a.AreaOfIt())


class Vehicle:
    max_speed = 220
    mileage = 12345612449064


class Vehicle2:
    pass


class Bus(Vehicle):
    pass
