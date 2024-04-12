# Importing the necessary classes from the abc module to create an abstract base class
from abc import ABC, abstractmethod

# Definition of the Battery class, which will serve as an abstract base class for all types of batteries
class Battery(ABC):
    # Declaration of an abstract method 'needs_service'. This method is intended to be overridden in any subclass.
    # The method will determine if a battery needs service based on specific criteria implemented in the subclasses.
    @abstractmethod
    def needs_service(self) -> bool:
        # The pass statement is a placeholder used because 'abstractmethod' cannot have a body. It forces subclasses to implement this method.
        pass
