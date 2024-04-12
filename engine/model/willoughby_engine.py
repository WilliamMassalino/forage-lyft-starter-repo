# Import the Engine class from the engine module. The Engine class likely provides a base set of features and behaviors that are common to all engines.
from engine import Engine

# Define the WilloughbyEngine class which inherits from the Engine class. This allows it to use or override functionality from the Engine base class.
class WilloughbyEngine(Engine):
    # Constructor method for initializing new instances of WilloughbyEngine
    def __init__(self, last_service_mileage, current_mileage):
        # Store the mileage at the last service; this is used to determine when the next service is due.
        self.last_service_mileage = last_service_mileage
        # Store the current mileage of the engine; this value is updated as the engine is used.
        self.current_mileage = current_mileage

    # Method to determine if the engine needs service based on its mileage.
    def needs_service(self) -> bool:
        # Return True if the difference between current mileage and last service mileage is greater than 60,000 miles, indicating that service is needed.
        return self.current_mileage - self.last_service_mileage > 60000
