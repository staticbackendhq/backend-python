"""StaticBackend Python 3 client."""

from .config import Config
from .errors import AuthenticationError, EmailError, HTTPRequestError, ValidationError
from .staticbackend import StaticBackend
from .version import __version__

__all__ = [
    "ValidationError",
    "AuthenticationError",
    "EmailError",
    "HTTPRequestError",
    "__version__",
    "Config",
    "StaticBackend",
]
