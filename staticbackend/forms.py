"""Submit forms."""

from typing import Any, Dict, Optional

from httpx import Client
from httpx._types import RequestFiles

from .base import Base


class Form(Base):
    def __init__(self, client: Client, token: str):
        super().__init__(client, token)

    def submit(
        self,
        name: str,
        data: Dict[str, Any] = None,
        files: Optional[RequestFiles] = None,
    ) -> bool:
        raise NotImplementedError()
