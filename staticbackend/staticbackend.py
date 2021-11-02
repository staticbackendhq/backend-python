"""StaticBackend class."""

from functools import lru_cache
from types import TracebackType
from typing import Optional, Type

from httpx import Client

from .config import Config
from .user import User
from .version import __version__


class StaticBackend(object):
    """
    StaticBackend is the base class for all staticbackend operations.
    """

    def __init__(self, config: Config):
        """f
        Initializes the StaticBackend class.f

        :param config: Configure for StaticBackend client.
        """
        self.api_token = config.api_token
        self.endpoint = config.endpoint
        self.root_token = config.root_token
        self._client = Client(
            headers={
                "SB-PUBLIC-KEY": f"{self.api_token}",
                "User-Agent": f"StaticBackend-Python/{__version__}",
            },
            base_url=self.endpoint,
        )

    def __enter__(self) -> "StaticBackend":
        """Context manager enter."""
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        """Context manager exit."""
        pass

    @property  # type: ignore
    @lru_cache()
    def user(self) -> User:
        """
        User management.

        :return: User management operations.
        """

        return User(self._client, self.root_token)
