# backend-python

[StaticBackend](https://staticbackend.com/) Python 3 client.

## Requirements

CPython 3.6.2+

## Installatin

```
pip install staticbackend
```

## Usage

```python
from staticbackend import Config, StaticBackend

config = Config(
    api_token=os.environ["PUBLICKEY"],
    root_token=os.environ["ROOTKEY"],
    endpoint=os.environ["ENDPOINT"],
)
backend = StaticBackend(config)
state = backend.user.login("foo@bar.com", "zot")
docs = state.database.list_documents(db)
print(docs)
```

## Features

- User Management
    - Register
    - Login
    - Reset Password
- Database
    - Create a document
    - List documents
    - Get a document
    - Query for documents
    - Update a document
    - Delete documents
- Storage
    - Upload files

## License

MIT

## Contributing

TBD.

## CHANGELOG

See [CHANGELOG.md](https://github.com/staticbackendhq/backend-python/blob/main/CHANGELOG.md)
