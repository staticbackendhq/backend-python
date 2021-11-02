"""Database as a Service."""
from typing import Any, Dict, List

from httpx import Client
from pydantic import BaseModel

from .base import Base
from .errors import RecordNotFoundError


class DocumentResults(BaseModel):
    page: int
    size: int
    total: int
    results: List[Dict[str, Any]]


class Database(Base):
    """Database as a Service API."""

    def __init__(self, client: Client, token: str) -> None:
        """Initialize the Database object."""
        super().__init__(client, token)

    def create_document(self, repo: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a document."""
        resp: Any = self._request(f"/db/{repo}", body=data)
        return resp  # type: ignore

    def list_documents(
        self, repo: str, page: int = 1, size: int = 25, desc: bool = False
    ) -> DocumentResults:
        """List all documents."""
        resp: Any = self._request(f"/db/{repo}", method="get")
        return DocumentResults(**resp)

    def get_document(self, repo: str, doc_id: str) -> Dict[str, Any]:
        resp: Any = self._request(f"/db/{repo}/{doc_id}", method="get")
        if isinstance(resp, str):
            raise RecordNotFoundError(doc_id)
        return resp  # type: ignore

    def query(
        self,
        repo: str,
        filters: List[Dict[str, Any]],
        page: int = 1,
        size: int = 25,
        desc: bool = False,
    ) -> Dict[str, Any]:
        resp: Any = self._request(f"/db/{repo}", body=filters)
        return resp  # type: ignore

    def update_document(
        self, repo: str, doc_id: str, doc: Dict[str, Any]
    ) -> Dict[str, Any]:
        resp: Any = self._request(f"/db/{repo}/{doc_id}", body=doc, method="put")
        if isinstance(resp, str):
            raise RecordNotFoundError(doc_id)
        return resp  # type: ignore

    def delete_document(self, repo: str, doc_id: str) -> int:
        resp: Any = self._request(f"/db/{repo}/{doc_id}", method="delete")
        return int(resp)
