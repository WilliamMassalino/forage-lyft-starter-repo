# Import the abstract base class Engine from the local package.
from .engine import Engine

# Import specific engine types from the local package.
# These are concrete implementations of the Engine class.
from .capulet_engine import CapuletEngine  # Capulet engine, specific criteria for service.
from .sternman_engine import SternmanEngine  # Sternman engine, service based on warning light.
from .willoughby_engine import WilloughbyEngine  # Willoughby engine, different service criteria.
