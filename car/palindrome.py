# Import the Car class from the car module within the current package.
from .car import Car
# Import the SternmanEngine class from the engine.model package.
from engine import SternmanEngine
# Import the SpindlerBattery class from the battery.model package.
from battery.model import SpindlerBattery

# Define the Palindrome class which inherits from the Car class.
class Palindrome(Car):
    # Constructor method with parameters for warning light status and last service date.
    def __init__(self, warning_light_is_on, last_service_date):
        # Initialize the engine attribute with a SternmanEngine instance,
        # passing the warning_light_is_on parameter to its constructor.
        self.engine = SternmanEngine(warning_light_is_on)
        # Initialize the battery attribute with a SpindlerBattery instance,
        # passing the last_service_date parameter to its constructor.
        self.battery = SpindlerBattery(last_service_date)

    # Define the needs_service method that returns True if either the engine or the battery needs service.
    def needs_service(self) -> bool:
        # Call needs_service on both the engine and battery. Return True if any call returns True.
        return self.engine.needs_service() or self.battery.needs_service()
