# Import the base Car class which Rorschach will extend.
from .car import Car
# Import the specific engine type Rorschach uses.
from engine.model import WilloughbyEngine
# Import the specific battery type Rorschach uses.
from battery.model import NubbinBattery

# Define the class Rorschach, which is a specific model of Car.
class Rorschach(Car):
    # Constructor method with parameters for mileage and service date information.
    def __init__(self, last_service_mileage, current_mileage, last_service_date):
        # Initialize the engine attribute with a WilloughbyEngine object,
        # passing mileage information relevant for determining service need.
        self.engine = WilloughbyEngine(last_service_mileage, current_mileage)
        # Initialize the battery attribute with a NubbinBattery object,
        # passing the last service date relevant for determining service need.
        self.battery = NubbinBattery(last_service_date)

    # Method to determine if the car needs service by checking if either
    # the engine or the battery needs service.
    def needs_service(self) -> bool:
        # Calls needs_service on both the engine and the battery.
        # Returns True if either component needs service, otherwise False.
        return self.engine.needs_service() or self.battery.needs_service()
