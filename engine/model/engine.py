# Import the necessary modules from Python's Abstract Base Classes (ABC) module.
from abc import ABC, abstractmethod

# Define an abstract class named 'Engine' which inherits from 'ABC'.
class Engine(ABC):
    # Define an abstract method 'needs_service'. This method is expected to be implemented
    # by any subclass of 'Engine'. The method signature indicates that it will return a boolean value.
    @abstractmethod
    def needs_service(self) -> bool:
        # The 'pass' keyword is used here as a placeholder. Since 'needs_service' is an abstract method,
        # it does not contain any implementation in this class. The implementation should be provided
        # by the subclasses of 'Engine'.
        pass