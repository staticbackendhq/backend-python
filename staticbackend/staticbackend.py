"""StaticBackend class."""

import asyncio
from types import TracebackType
from typing import Any, Dict, Optional, Type, Union

from httpx import Client
from pydantic import EmailStr, validate_arguments

from .config import Config
from .errors import AuthencationError, HTTPRequestError
from .version import __version__


class StaticBackend(object):
    """
    StaticBackend is the base class for all staticbackend operations.
    """

    def __init__(
        self, config: Config, loop: Optional[asyncio.AbstractEventLoop] = None
    ):
        """f
        Initializes the StaticBackend class.f

        :param config: Configure for StaticBackend client.f
        :param loop: Python `asyncio` Event loop.
        """
        self.api_token = config.api_token
        self.endpoint = config.endpoint
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

    def _request(
        self, uri: str, body: Dict[str, Any], token: Optional[str] = None
    ) -> Union[Dict[str, Any], str, None]:
        """
        Make a request to the StaticBackend API.
        """

        headers = None
        if token is not None:
            headers = {"Authorization": f"Bearer {self.api_token}"}
        try:
            resp = self._client.post(uri, json=body, headers=headers)
        except Exception as e:
            raise HTTPRequestError(f"{e}") from e

        if resp.status_code == 401:
            raise AuthencationError()
        if "application/json" in resp.headers["content-type"]:
            d: Dict[str, Any] = resp.json()
            return d
        if "text/plain" in resp.headers["content-type"]:
            return resp.text
        return None

    def _user(self, uri: str, email: str, password: str) -> str:
        resp: Any = self._request(uri, {"email": email, "password": password})
        return resp  # type: ignore

    @validate_arguments
    def register(
        self,
        email: EmailStr,
        password: str,
    ) -> str:
        """Register new user.

        :param email: User’s email address
        :param password: User’s password
        :return: User’s authentication token
        :raises HTTPRequestError: if the http request have something wrong
        :raises AuthencationError: if the api_token is not valid
        :raises EmailError: if the email is not valid
        """
        return self._user("/register", email, password)

    @validate_arguments
    def login(
        self,
        email: EmailStr,
        password: str,
    ) -> str:
        """Validate user by email and password to receive their id and session token.

        :param email: User’s email address
        :param password: User’s password
        :return: User’s authentication token
        :raises HTTPRequestError: if the http request have something wrong
        :raises AuthencationError: if the api_token is not valid
        :raises EmailError: if the email is not valid
        """
        return self._user("/login", email, password)

    @validate_arguments
    def reset_password(
        self,
        token: str,
        email: EmailStr,
        old_password: str,
        new_password: str,
    ) -> bool:
        """Reset user password.

        :param email: User’s email address
        :param password: User’s password
        :return: User’s authentication token
        :raises HTTPRequestError: if the http request have something wrong
        :raises AuthencationError: if the api_token is not valid
        :raises EmailError: if the email is not valid
        """
        return True
