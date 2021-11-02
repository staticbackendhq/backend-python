# Welcome to StaticBackend Python Client

## Install

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

- [x] User Management
    - [x] Register
    - [x] Login
    - [x] Reset Password
- [x] Database
    - [x] Create a document
    - [x] List documents
    - [x] Get a document
    - [x] Query for documents
    - [x] Update a document
    - [x] Delete documents
- [x] Storage
    - [x] Upload files
- [ ] Forms
    - [ ] Submit HTML forms
- [ ] Websocket

## License

MIT

## Contributing

TBD.

## CHANGELOG

See [CHANGELOG.md](https://github.com/staticbackendhq/backend-python/blob/main/CHANGELOG.md)
