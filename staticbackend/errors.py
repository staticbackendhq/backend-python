"""Errors."""

from pydantic import ValidationError

__all__ = ("ValidationError",)


class Error(Exception):
    def __init__(self, message: str):
        self.message: str = message

    def __str__(self) -> str:
        return self.message


class AuthenticationError(Error):
    def __init__(self, message: str = "invalid StaticBackend public key"):
        super().__init__(message)


class LoginError(Error):
    def __init__(self, message: str = "invalid login credentials."):
        super().__init__(message)


class HTTPRequestError(Error):
    def __init__(self, message: str):
        super().__init__(
            message=message,
        )


class EmailError(Error):
    def __init__(self, message: str = "Invalid email"):
        super().__init__(
            message=message,
        )


class RecordNotFoundError(Error):
    def __init__(self, doc_id: str):
        super().__init__(
            message=f"Record {doc_id} not found",
        )
