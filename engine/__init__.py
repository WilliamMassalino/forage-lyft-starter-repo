# Import the abstract base class Engine from the local package.
from engine.engine import Engine

# Import specific engine types from the local package.
# These are concrete implementations of the Engine class.
from .model.capulet_engine import CapuletEngine  # Capulet engine, specific criteria for service.
from .model.sternman_engine import SternmanEngine  # Sternman engine, service based on warning light.
from .model.willoughby_engine import WilloughbyEngine  # Willoughby engine, different service criteria.
