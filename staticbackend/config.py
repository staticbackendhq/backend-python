"""Configure for StaticBackend client."""

from pydantic import BaseModel, Field, HttpUrl, validator


class Config(BaseModel):
    """Configure staticbackend."""

    api_token: str = Field(..., title="API Token for StaticBackend")
    root_token: str = Field(..., title="Root Token for StaticBackend")
    endpoint: HttpUrl = Field(
        default="http://localhost:8099", title="StaticBackend API endpoint"
    )

    @validator("api_token")
    def check_api_token(cls, v: str) -> str:
        """Validate API Token."""
        if not v:
            raise ValueError("API Token cannot be empty")
        return v

    @validator("root_token")
    def check_root_token(cls, v: str) -> str:
        """Validate API Token."""
        if not v:
            raise ValueError("ROOT Token cannot be empty")
        return v
