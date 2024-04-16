# Import the car model classes from their respective modules. Each class represents a specific model of car.
from car.calliope import Calliope
from car.glissade import Glissade
from car.palindrome import Palindrome
from car.rorschach import Rorschach
from car.thovex import Thovex
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

# Define the CarFactory class, which is responsible for creating instances of different car models.
class CarFactory:
    # A static method to create an instance of the Calliope model.
    # This method does not depend on the state of the CarFactory class (hence static),
    # and directly returns a new instance of Calliope.
    @staticmethod
    def create_calliope(last_service_mileage, current_mileage, last_service_date,tire_wear_array):
        return Calliope(last_service_mileage, current_mileage, last_service_date,tire_wear_array)
    
    # A method to create an instance of the Glissade model.
    # This method is not static because it uses 'self', which refers to an instance of CarFactory,
    # though it could be marked as static as well since it doesn't use the 'self' parameter.
    def create_glissade(last_service_mileage, current_mileage, last_service_date,tire_wear_array):
        return Glissade(last_service_mileage, current_mileage, last_service_date,tire_wear_array)
    
    # A method to create an instance of the Palindrome model.
    # Similar to create_glissade, it could also be marked as static as it doesn't utilize 'self'.
    def create_palindrome(last_service_mileage, current_mileage, last_service_date,tire_wear_array):
        return Palindrome(last_service_mileage, current_mileage, last_service_date,tire_wear_array)
    
    # A method to create an instance of the Rorschach model.
    # It follows the same pattern as the other methods, creating and returning a new car instance.
    def create_rorschach(last_service_mileage, current_mileage, last_service_date,tire_wear_array):
        return Rorschach(last_service_mileage, current_mileage, last_service_date,tire_wear_array)
    
    # A method to create an instance of the Thovex model.
    # Consistent with other methods, it instantiates and returns a new Thovex car.
    def create_thovex(last_service_mileage, current_mileage, last_service_date,tire_wear_array):
        return Thovex(last_service_mileage, current_mileage, last_service_date,tire_wear_array)
