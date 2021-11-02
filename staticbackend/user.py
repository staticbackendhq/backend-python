"""User management."""

from functools import lru_cache
from typing import Any

from httpx import Client

from .base import Base
from .database import Database
from .errors import EmailError, LoginError
from .forms import Form
from .storage import Storage


class LoginState(Base):
    def __init__(self, client: Client, token: str) -> None:
        super().__init__(client, token)
        self.token = token

    @property  # type: ignore
    @lru_cache()
    def database(self) -> Database:
        return Database(self.client, self.token)  # type: ignore

    @property  # type: ignore
    @lru_cache()
    def forms(self) -> Form:
        return Form(self.client, self.token)  # type: ignore

    @property  # type: ignore
    @lru_cache()
    def storage(self) -> Storage:
        return Storage(self.client, self.token)  # type: ignore


class User(Base):
    def __init__(self, client: Client, root_token: str = None) -> None:
        super().__init__(client, root_token)

    def _user(self, uri: str, email: str, password: str) -> str:
        resp: Any = self._request(uri, {"email": email, "password": password})
        return resp  # type: ignore

    def register(
        self,
        email: str,
        password: str,
    ) -> LoginState:
        """Register new user.

        :param email: User’s email address
        :param password: User’s password
        :return: User’s authentication token
        """
        token = self._user("/register", email, password)
        if "invalid email" in token:
            raise EmailError()
        return LoginState(self.client, token)

    def login(
        self,
        email: str,
        password: str,
    ) -> LoginState:
        """Validate user by email and password to receive their id and session token.

        :param email: User’s email address
        :param password: User’s password
        :return: User’s authentication token
        """
        token = self._user("/login", email, password)
        if "no documents in result" in token:
            raise LoginError()
        return LoginState(self.client, token)

    def send_reset_code(
        self,
        email: str,
    ) -> str:
        """Send reset code to user's email.

        :param email: User’s email address
        :return: Reset code.
        """
        resp: Any = self._request(
            "/password/resetcode", method="get", params={"e": email}
        )
        if "invalid email" in resp:
            raise EmailError()
        return resp  # type: ignore

    def reset_password(
        self,
        email: str,
        code: str,
        password: str,
    ) -> bool:
        """Reset user password.

        :param email: User’s email address
        :param code: User’s reset code
        :param password: User’s new password
        :return: Reset or not
        """
        resp: Any = self._request(
            "/password/reset",
            body={"email": email.lower(), "code": code, "password": password},
        )
        return resp  # type: ignore
