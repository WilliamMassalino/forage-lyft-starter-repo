# Import necessary classes from Python's abc module which supports the creation of abstract base classes
from abc import ABC, abstractmethod

# Define an abstract base class named 'Car'. An abstract class is a class that cannot be instantiated on its own
# and is intended to be subclassed by other classes.
class Car(ABC):
    # Declare an abstract method 'needs_service'. Abstract methods are declared, but they contain no implementation.
    # Subclasses are expected to implement this method. The method is intended to return a boolean value, hence the -> bool.
    @abstractmethod
    def needs_service(self) -> bool:
        # The 'pass' statement is a placeholder. Since this is an abstract method, it does not perform any action
        # and thus has no body. Subclasses will provide their own specific implementation of this method.
        pass
