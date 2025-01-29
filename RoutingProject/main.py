import truck
import csv
import datetime

from hash import ChainingHashTable
from package import Package


#Read all CSV files with 3 following methods
with open("distanceCSV.csv") as csvfile0:
    csvDistance = csv.reader(csvfile0)
    csvDistance = list(csvDistance)

with open("addressCSV.csv") as csvfile1:
    csvAddress = csv.reader(csvfile1)
    csvAddress = list(csvAddress)

with open("packageCSV.csv") as csvfile2:
    csvPackage = csv.reader(csvfile2)
    csvPackage = list(csvPackage)


#Create package objects from files
#Load package objects into hash table
def loadPackageData(fileName, packageHashTable):
    with open(fileName) as packageInfo:
        packageData = csv.reader(packageInfo)
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pStatus = "At Hub"

            #Create Package object
            p = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pWeight, pStatus)

            #Insert data into hash table
            packageHashTable.insert(pID, p)


#Assign Hash Table
packageHashTable = ChainingHashTable()


#Method for finding distance between addresses
def distanceBetween(addy0, addy1):
    distance = csvDistance[addy0][addy1]
    if distance == '':
        distance = csvDistance[addy1][addy0]
    return float(distance)


#Method to find minimum distance to next address
def loadAddressData(addy):
    for row in csvAddress:
        if addy in row[2]:
            return int(row[0])


#Create 1st truck object
truck1 = truck.Truck(18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))

#Create 2nd truck object
truck2 = truck.Truck(18, None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

#Create 3rd truck object
truck3 = truck.Truck(18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9, minutes=5))


#Load package data to Hash Table
loadPackageData("packageCSV.csv", packageHashTable)


#Method for delivering packages on each truck using nearest neighbor algorithm
#Calculate distance each truck drives after deliveries
def deliverPackages(trucks):
    notDelivered = []
    for packageID in trucks.packages:
        package = packageHashTable.search(packageID)
        notDelivered.append(package)
    #Clear package list so trucks can be stocked in correct order per nearest neighbor
    trucks.packages.clear()


 #Cycle through entire list of notDelivered until completed
    while len(notDelivered) > 0:
        nextAddress = 2000
        nextPackage = None
        for package in notDelivered:
            if distanceBetween(loadAddressData(trucks.address), loadAddressData(package.address)) <= nextAddress:
                nextAddress = distanceBetween(loadAddressData(trucks.address), loadAddressData(package.address))
                nextPackage = package
        trucks.packages.append(nextPackage.ID)
        notDelivered.remove(nextPackage)
        trucks.mileage += nextAddress
        trucks.address = nextPackage.address
        trucks.time += datetime.timedelta(hours=nextAddress / 18)
        nextPackage.deliveryTime = trucks.time
        nextPackage.departTime = trucks.departTime


#Send trucks through delivery process
deliverPackages(truck1)
deliverPackages(truck3)
#Make sure truck2 does not leave until truck1 and truck2 are finished
truck2.departTime = min(truck1.departTime, truck3.departTime)
deliverPackages(truck2)


#UI to interact with user
print("Welcome to the Parcel Serivce Portal!", "\n")
print("The total mileage for the route is:", "\n")
#Calculate total mileage
print((truck1.mileage + truck2.mileage + truck3.mileage), "\n")
#Method for finding/printing package info
while True:
    #Enter time to check status, specify data input
    userTime = input("Please enter time (HH:MM) of status check or enter X to exit: ")
    if userTime == "X" or userTime == "x":
        break
    else:
        (h, m) = userTime.split(":")
        timeChange = datetime.timedelta(hours=int(h), minutes=int(m))
    try:
        print("\n")
        #Enter package ID or nothing
        specificEntry = [int(input("Enter Package ID or click enter: "))]
        print("\n")
        print("Results:")
    #Specify ID range
    except ValueError:
        specificEntry = range(1, 41)
    #Find ID and print
    for packageID in specificEntry:
        package = packageHashTable.search(packageID)
        package.newStatus(timeChange)
        if packageID in truck1.packages:
            truckNum = 1
        elif packageID in truck2.packages:
            truckNum = 2
        else:
            truckNum = 3
        print(str(package), int(truckNum))
