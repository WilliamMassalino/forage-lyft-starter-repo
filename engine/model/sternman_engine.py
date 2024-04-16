# Import the abstract base class Engine from the engine module.
from engine.engine import Engine

# Define a class SternmanEngine, which inherits from the Engine class.
class SternmanEngine(Engine):
    # Constructor method with self representing the instance of the object itself
    # and warning_light_is_on as a boolean parameter to indicate the status of the warning light.
    def __init__(self, warning_light_is_on):
        # Set the instance variable warning_light_is_on to the value passed to the constructor.
        # This variable tracks whether the warning light on the engine is on or off.
        self.warning_light_is_on = warning_light_is_on

    # Define a method to determine if this type of engine needs service.
    # This is a concrete implementation of the abstract method defined in the Engine class.
    def needs_service(self) -> bool:
        # Return True if the warning light is on, indicating service is needed.
        # Otherwise, return False.
        return self.warning_light_is_on
