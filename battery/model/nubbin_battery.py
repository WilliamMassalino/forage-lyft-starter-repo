# Import the datetime module to handle date operations
from datetime import datetime
# Import the abstract Battery class from the current package
from .battery import Battery

# Define the NubbinBattery class which inherits from the Battery class
class NubbinBattery(Battery):
    # Constructor method for initializing a new instance of NubbinBattery
    def __init__(self, last_service_date):
        # Store the last service date of the battery
        self.last_service_date = last_service_date

    # Method to determine if the battery needs service
    def needs_service(self) -> bool:
        # Calculate the date 4 years after the last service date
        service_due_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        # Check if the current date is past the service due date
        return service_due_date < datetime.now().date()
