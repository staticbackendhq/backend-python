"""StaticBackend Python 3 client."""

from .config import Config
from .staticbackend import StaticBackend
from .errors import ValidationError
from .version import __version__

__all__ = ["ValidationError", "__version__"]
