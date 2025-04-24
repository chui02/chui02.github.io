import uuid #Generates random ID numbers as placeholders
import time #Simulating real-world info
from random import randint #Similarly generates random ints as placeholders (Such as price for car ride)

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.rideHistory = []

class Driver:
    def __init__(self, driverID, name, location):
        self.driverID = driverID
        self.name = name
        self.location = location
        self.available = True

class Ride:
    def __init__(self, rideID, user, driver, pickup, drop):
        self.rideID = rideID
        self.user = user
        self.driver = driver
        self.pickup = pickup
        self.drop = drop
        self.start_time = time.time()
        self.end_time = None
        self.status = "Booked"
        self.price = randint(5, 30) #Just a random price for getting a ride done

    def finishRide(self):
        self.end_time = time.time()
        self.status = "Completed"

    def cancelRide(self):
        self.status = "Cancelled"

class RideService:
    def __init__(self):
        self.rides = {}

    def bookRide(self, user, driver, pickup, drop):
        rideID = str(uuid.uuid4())
        ride = Ride(rideID, user, driver, pickup, drop)
        self.rides[rideID] = ride
        user.rideHistory.append(ride)
        driver.available = False
        return ride

    def cancelRide(self, rideID):
        if rideID in self.rides:
            ride = self.rides[rideID]
            ride.cancelRide()
            ride.driver.available = True
            return True
        return False

class DriverService:
    def __init__(self):
        self.drivers = []

    def registeredDriver(self, name, location):
        driver = Driver(str(uuid.uuid4()), name, location)
        self.drivers.append(driver)

    def findDrivers(self, userLocation):
        return [d for d in self.drivers if d.available]

class UserService:
    def __init__(self):
        self.users = {}

    def registeredUser(self, name):
        user = User(str(uuid.uuid4()), name)
        self.users[user.user_id] = user
        return user

class PaymentService:
    def paymentFinish(self, ride):
        print(f"Processing payment of ${ride.price} for {ride.user.name}...")

userServices = UserService()
registeredDriver = DriverService()
riderServices = RideService()
paymentServices = PaymentService()

#Registered user and drivers
exampleUser = userServices.registeredUser("Joe")
registeredDriver.registeredDriver("Sam", "Area A")
registeredDriver.registeredDriver("Ashley", "Area A")

#Getting a ride
drivers = registeredDriver.findDrivers("Area A")
ride = riderServices.bookRide(exampleUser, drivers[0], "Area A", "Area B")
print(f"Ride booked: {ride.rideID}, Driver: {ride.driver.name}")

#Finishing a given ride
ride.finishRide()
paymentServices.paymentFinish(ride)

#Viewing history
for r in exampleUser.rideHistory:
    print(f"{r.status} ride from {r.pickup} to {r.drop}, cost: ${r.price}")
