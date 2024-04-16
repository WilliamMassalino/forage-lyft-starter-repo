import unittest
# Import the engine classes from the engine module.
from engine.model.capulet_engine import CapuletEngine
from engine.model.sternman_engine import SternmanEngine
from engine.model.willoughby_engine import WilloughbyEngine
# Import the battery classes from the battery module.
from battery.model.battery import Battery
from unittest.mock import patch
# Import the tire classes from the tire module.
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine = CapuletEngine(last_service_mileage=0, current_mileage=30001)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = CapuletEngine(last_service_mileage=0, current_mileage=30000)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine = WilloughbyEngine(last_service_mileage=0, current_mileage=60001)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = WilloughbyEngine(last_service_mileage=0, current_mileage=60000)
        self.assertFalse(engine.needs_service())

class TestBattery(unittest.TestCase):
    def test_subclass_must_implement_needs_service(self):
        with self.assertRaises(TypeError):
            # Attempt to create a dummy class that inherits from Battery but does not implement the abstract methods.
            # This should raise a TypeError because we cannot instantiate an abstract class without defining all of its abstract methods.
            class DummyBattery(Battery):
                pass
            DummyBattery()

    @patch.multiple(Battery, __abstractmethods__=set())
    def test_concrete_subclass_can_be_instantiated(self):
        # By patching __abstractmethods__ to an empty set, we make Battery temporarily 'concrete'.
        # We then define a dummy class that should be instantiable because Battery no longer has any abstract methods.
        class InstantiableBattery(Battery):
            def needs_service(self):
                return True

        # We should be able to instantiate the class without any issue.
        battery = InstantiableBattery()
        self.assertIsInstance(battery, Battery)
        self.assertTrue(battery.needs_service())

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_array = [0.1, 0.4, 0.9, 0.2]
        tire = CarriganTire(tire_wear_array)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear_array = [0.1, 0.4, 0.2, 0.2]
        tire = CarriganTire(tire_wear_array)
        self.assertFalse(tire.needs_service())

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_array = [0.8, 0.8, 0.8, 0.8]
        tire = OctoprimeTire(tire_wear_array)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear_array = [0.5, 0.5, 0.5, 0.5]
        tire = OctoprimeTire(tire_wear_array)
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()