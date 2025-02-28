#- Attributes: brand, model, year, rental_price_per_day
#- Methods:
#display_info(): Prints vehicle details.
#calculate_rental_cost(days): Returns the rental cost for a given number of days.(inherits from Vehicle):
#Additional attribute: seating_capacity
#Override display_info() to include seating capacity. (inherits from Vehicle)
#Additional attribute: engine_capacity
#Override display_info() to include engine capacity.
#Make rental_price_per_day a private attribute.
#Provide a setter and getter method for rental_price_per_day.
#Create a function show_vehicle_info(vehicle) that takes a Vehicle object and calls display_info(), demonstrating polymorphism.
#Create instances of Car and Bike with sample data.
#Display their details using display_info().
#Calculate rental costs for a given number of days.
#Modify rental prices using setter methods and display the updated price.

#define super class vehicle
class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day #private attribute

#display vehicle details
    def display_info(self):
        print(f"{self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.__rental_price_per_day}/day")

#calculate rental cost
    def calculate_rental_cost(self, days):
        return days * self.__rental_price_per_day

#setter and getter for rental price
    def set_rental_price_per_day(self, price):
        self.__rental_price_per_day = price

    def get_rental_price_per_day(self):
        return self.__rental_price_per_day

#sub class car    
class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self.get_rental_price_per_day()}/day")

#sub class bike
class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine Capacity: {self.engine_capacity}, Rental Price: ${self.get_rental_price_per_day()}/day")

#function to demonstrate polymorphism by calling the display_info method on any Vehicle object.
def show_vehicle_info(vehicle):
        vehicle.display_info()

car = Car("Toyota", "Corolla", 2019, 50, 5)
bike = Bike("Honda", "CD70", 2020, 20, "70cc")

#display vehicles details
car.display_info()
bike.display_info()

#calculate rental cost
print(f"Rental cost for 3 days: ${car.calculate_rental_cost(3)}")
print(f"Rental cost for 5 days: ${bike.calculate_rental_cost(5)}")

#modify rental prices
car.set_rental_price_per_day(55)
bike.set_rental_price_per_day(35)

#display updated rental prices
print("\nUpdated rental prices:")
car.display_info()
bike.display_info()

