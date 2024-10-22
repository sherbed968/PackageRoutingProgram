#Create Package class

import datetime

class Package:
    def __init__(self, ID, address, city, state, zip, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departTime = None
        self.deliveryTime = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip,
                                                       self.deadline, self.weight, self.deliveryTime,
                                                       self.status)
        
    def newStatus(self, newTime):
        if self.deliveryTime == None:
            self.status = "At the hub - Truck"
        elif newTime < self.departTime:
            self.status = "At the hub - Truck"
        elif newTime < self.deliveryTime:
            self.status = "En route - Truck"
        else:
            self.status = "Delivered - Truck"
        # Change address for package 9 once it's been received
        if self.ID == 9:
            if newTime > datetime.timedelta(hours=10, minutes=20):
                self.address = "410 S State St"
                self.zip = "84111"
            else:
                self.address = "300 State St"
                self.zip = "84103"
