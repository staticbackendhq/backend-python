"""."""

from typing import Any, Dict, Optional, Union

from httpx import Client

from .errors import AuthencationError, HTTPRequestError


class Base(object):
    def __init__(self, client: Client) -> None:
        super().__init__()
        self.client = client

    def _request(
        self, uri: str, body: Dict[str, Any], token: Optional[str] = None
    ) -> Union[Dict[str, Any], str, None]:
        """
        Make a request to the StaticBackend API.
        """

        headers = None
        if token is not None:
            headers = {"Authorization": f"Bearer {token}"}
        try:
            resp = self.client.post(uri, json=body, headers=headers)
        except Exception as e:
            raise HTTPRequestError(f"{e}") from e

        if resp.status_code == 401:
            raise AuthencationError()

        if "application/json" in resp.headers["content-type"]:
            d: Dict[str, Any] = resp.json()
            return d
        if "text/plain" in resp.headers["content-type"]:
            text: str = resp.text
            return text
        return None
