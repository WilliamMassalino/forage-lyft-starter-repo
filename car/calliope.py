# Importing the base Car class to inherit from.
from .car import Car
# Importing the specific Engine and Battery types this car model uses.
from engine import CapuletEngine
from battery.model import SpindlerBattery
from tire.tire import CarriganTire, OctoprimeTire

# Define the class Calliope, which is a specific type of Car.
class Calliope(Car):
    # Constructor method for initializing a new instance of Calliope.
    def __init__(self, last_service_mileage, current_mileage, last_service_date):
        # Initialize the engine attribute with a CapuletEngine, passing in the
        # last service mileage and the current mileage.
        self.engine = CapuletEngine(last_service_mileage, current_mileage)
        # Initialize the battery attribute with a SpindlerBattery, passing in
        # the last service date.
        self.battery = SpindlerBattery(last_service_date)
        self.tires = [CarriganTire(), OctoprimeTire()]  

    # Method to determine if the Calliope needs servicing.
    def needs_service(self) -> bool:
        # Returns True if either the engine or the battery needs service.
        # This checks both the engine's and the battery's own service logic.
        return self.engine.needs_service() or self.battery.needs_service() or self.engine.needs_service()
