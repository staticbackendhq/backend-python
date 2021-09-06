"""Errors."""

from pydantic import ValidationError

__all__ = ("ValidationError",)


class Error(Exception):
    def __init__(self, message: str):
        self.message: str = message

    def __str__(self) -> str:
        return self.message


class AuthencationError(Error):
    def __init__(self, message: str = "invalid StaticBackend public key"):
        super().__init__(message)


class HTTPRequestError(Error):
    def __init__(self, message: str):
        super().__init__(
            message=message,
        )


class EmailError(Error):
    def __init__(self, message: str):
        super().__init__(
            message=message,
        )
