# Import the Engine base class from the engine module. This class is likely to define a common interface for all engine types.
from engine import Engine

# Define the CapuletEngine class, which inherits from the Engine class.
class CapuletEngine(Engine):
    # The constructor method, __init__, initializes an instance of the CapuletEngine class.
    def __init__(self, last_service_mileage, current_mileage):
        # Instance variable 'last_service_mileage' stores the mileage at the car's last service.
        self.last_service_mileage = last_service_mileage
        # Instance variable 'current_mileage' stores the car's current mileage.
        self.current_mileage = current_mileage

    # Method to determine if the engine needs servicing. It returns a boolean value.
    def needs_service(self) -> bool:
        # Check if the difference between the current mileage and the last service mileage exceeds 30,000 miles.
        # Returns True if the engine needs service, False otherwise.
        return self.current_mileage - self.last_service_mileage > 30000
