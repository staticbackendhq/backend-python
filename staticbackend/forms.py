"""Submit forms."""

from typing import Dict

from httpx import Client

from .base import Base


class Form(Base):
    def __init__(self, client: Client, token: str):
        super().__init__(client, token)

    def submit(self, name: str, data: Dict[str, str]) -> bool:
        """Submit HTML forms."""
        try:
            self.client.post(f"/postform/{name}", data=data)
            return True
        except Exception:
            return False
