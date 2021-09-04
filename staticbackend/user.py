"""User management."""

from typing import Any

from httpx import Client

from .base import Base


class User(Base):
    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def _user(self, uri: str, email: str, password: str) -> str:
        resp: Any = self._request(uri, {"email": email, "password": password})
        return resp  # type: ignore

    def register(
        self,
        email: str,
        password: str,
    ) -> str:
        """Register new user.

        :param email: User’s email address
        :param password: User’s password
        :return: User’s authentication token
        """
        return self._user("/register", email, password)

    def login(
        self,
        email: str,
        password: str,
    ) -> str:
        """Validate user by email and password to receive their id and session token.

        :param email: User’s email address
        :param password: User’s password
        :return: User’s authentication token
        """
        return self._user("/login", email, password)

    def _reset(self, uri: str, body: dict) -> bool:
        resp: Any = self._request(uri, body)
        return resp.lower() == "true"  # type: ignore

    def send_reset_code(
        self,
        email: str,
    ) -> bool:
        """Send reset code to user's email.

        :param email: User’s email address
        :return: Send or not
        """
        return self._reset("/password/send", {"email": email})

    def reeset_password(
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
        return self._reset(
            "/password/reset", {"email": email, "code": code, "password": password}
        )
