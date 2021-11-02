"""Base utils."""

from typing import Any, Dict, List, Optional, Union

from httpx import Client
from httpx._types import RequestFiles

from .errors import AuthenticationError, HTTPRequestError


class Base(object):
    def __init__(self, client: Client, token: Optional[str]) -> None:
        super().__init__()
        self.token = token
        self.client = client

    def _request(
        self,
        uri: str,
        body: Union[Dict[str, Any], List[Dict[str, Any]], None] = None,
        params: Optional[Dict[str, Any]] = None,
        files: Optional[RequestFiles] = None,
        data: Optional[Dict[str, Any]] = None,
        method: str = "post",
    ) -> Union[Dict[str, Any], str, None]:
        """
        Make a request to the StaticBackend API.
        """

        headers = None
        if self.token is not None:
            headers = {"Authorization": f"Bearer {self.token}"}
        try:
            resp = self.client.request(
                method,
                uri,
                json=body,
                params=params,
                data=data,
                files=files,
                headers=headers,
                timeout=10,
            )
        except Exception as e:
            raise HTTPRequestError(f"{e}") from e

        if resp.status_code == 401:
            raise AuthenticationError()

        if "application/json" in resp.headers["content-type"]:
            d: Dict[str, Any] = resp.json()
            return d
        if "text/plain" in resp.headers["content-type"]:
            text: str = resp.text
            return text
        return None
