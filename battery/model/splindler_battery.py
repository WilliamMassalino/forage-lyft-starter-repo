# Import the datetime class from the datetime module to work with dates
from datetime import datetime
# Import the abstract base class Battery from the local package
from .battery import Battery

# Define a new class SpindlerBattery that inherits from the Battery class
class SpindlerBattery(Battery):
    # Constructor method with initialization of the class
    def __init__(self, last_service_date):
        # Store the last service date provided during instantiation
        self.last_service_date = last_service_date

    # Method to determine if the battery needs service
    def needs_service(self) -> bool:
        # Increment the last service year by 2 and compare it to today's date
        # If the date after adding two years is earlier than today, return True (needs service)
        # Otherwise, return False (does not need service)
        return self.last_service_date.replace(year=self.last_service_date.year + 2) < datetime.now().date()
