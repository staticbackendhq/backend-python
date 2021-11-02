"""Submit forms."""


from typing import IO, Any, Dict, Optional, Union

from httpx import Client

from .base import Base


class Storage(Base):
    def __init__(self, client: Client, token: str):
        super().__init__(client, token)

    def upload_file(self, fn: str) -> Dict[str, str]:
        """Upload files via filename."""
        with open(fn, "rb") as f:
            resp: Any = self._request("/storage/upload", files={"file": (fn, f, None)})
            return resp  # type: ignore

    def upload(
        self, data: Union[IO[bytes], bytes], fn: Optional[str] = None
    ) -> Dict[str, str]:
        """Upload content."""
        resp: Any = self._request("/storage/upload", files={"file": (fn, data, None)})
        return resp  # type: ignore
