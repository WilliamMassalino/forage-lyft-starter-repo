# Import the Car class from the current package's car module.
from .car import Car
# Import the WilloughbyEngine class from the engine.model package.
from engine import WilloughbyEngine
# Import the SpindlerBattery class from the battery.model package.
from battery.model import SpindlerBattery

# Define the Glissade class, which inherits from the Car class.
class Glissade(Car):
    # Constructor method with parameters for service mileage and dates.
    def __init__(self, last_service_mileage, current_mileage, last_service_date):
        # Initialize the engine attribute with a WilloughbyEngine object, passing in mileage data.
        self.engine = WilloughbyEngine(last_service_mileage, current_mileage)
        # Initialize the battery attribute with a SpindlerBattery object, passing in the last service date.
        self.battery = SpindlerBattery(last_service_date)

    # Define a method to check if the car needs servicing.
    def needs_service(self) -> bool:
        # Return True if either the engine or battery requires service.
        return self.engine.needs_service() or self.battery.needs_service()
