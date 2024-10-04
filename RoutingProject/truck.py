#Create Truck class
class Truck:
    def __init__(self, speed, load, packages, mileage, address, departTime):
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.departTime = departTime
        self.time = departTime

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.speed, self.load, self.packages, self.mileage,
                                               self.address, self.departTime)