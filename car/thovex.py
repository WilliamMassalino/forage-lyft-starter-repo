# Import the Car base class to inherit from.
from .car import Car

# Import the specific Engine and Battery models that Thovex uses.
from engine.model import CapuletEngine
from battery.model import NubbinBattery

# Define the Thovex class, which is a specific model of Car.
class Thovex(Car):
    # Constructor method for initializing a new instance of Thovex.
    def __init__(self, last_service_mileage, current_mileage, last_service_date):
        # Initialize the engine attribute with a CapuletEngine instance.
        # The CapuletEngine requires last service mileage and current mileage to determine if it needs service.
        self.engine = CapuletEngine(last_service_mileage, current_mileage)
        
        # Initialize the battery attribute with a NubbinBattery instance.
        # The NubbinBattery requires the last service date to determine if it needs service.
        self.battery = NubbinBattery(last_service_date)

    # Define a method to determine if the Thovex car needs service.
    def needs_service(self) -> bool:
        # Check if either the engine or the battery needs service and return True if so.
        return self.engine.needs_service() or self.battery.needs_service()
