# Import necessary classes from Python's abc module which supports the creation of abstract base classes
from abc import ABC, abstractmethod
from tire.tire import Tire
from engine.engine import Engine
from battery.model import Battery
# Define an abstract base class named 'Car'. An abstract class is a class that cannot be instantiated on its own
# and is intended to be subclassed by other classes.
class Car(ABC):
    def __init__(self, engine, battery, tire):
        self.tire = tire # Add the tire attribute
        self.engine = engine
        self.battery = battery
    # Declare an abstract method 'needs_service'. Abstract methods are declared, but they contain no implementation.
    # Subclasses are expected to implement this method. The method is intended to return a boolean value, hence the -> bool.
    @abstractmethod
    def needs_service(self) -> bool:
        # The 'pass' statement is a placeholder. Since this is an abstract method, it does not perform any action
        # and thus has no body. Subclasses will provide their own specific implementation of this method.
        return (self.engine.needs_service() or 
                self.battery.needs_service() or 
                self.tire.needs_service() 
        )
