# StaticBackend

## Reference

### staticbackend.staticbackend.StaticBackend

#### `__init__(self, config: Config)`

: __config__: _Required_. StaticBackend configure.

#### `user`

`user` property return [`staticbackend.user.User`](#staticbackenduseruser) to access login or register.

### staticbackend.user.User

#### `register(self, email: str, password: str)`

: __email__: _Required_. User email.
: __password__: _Required_. User password.

#### `login(self, email: str, password: str)`

: __email__: _Required_. User email.
: __password__: _Required_. User password.

### staticbackend.user.LoginState

#### `token`

`token` property return auth token.

#### `database`

`database` property return [`staticbackend.database.Database`](#staticbackenddatabasedatabase).

#### `storage`

`storage` property return [`staticbackend.storage.Storage`](#staticbackendstoragestorage).

### staticbackend.database.Database

#### `create_document(self, repo: str, data: Dict[str, Any])`

#### `update_document(self, repo: str, doc_id: str, doc: Dict[str, Any])`

#### `list_documents(self, repo: str, page: int = 1, size: int = 25, desc: bool = False)`

#### `get_document(self, repo: str, doc_id: str)`

#### `query(self, repo: str, filters: List[Dict[str, Any]], page: int = 1, size: int = 25, desc: bool = False)`

#### `delete_document(self, repo: str, doc_id: str)`

### staticbackend.storage.Storage

#### `upload_file(self, fn: str)`

#### `upload(self, data: Union[IO[bytes], bytes], fn: Optional[str] = None)`
