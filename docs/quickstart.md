# Quick Start

## Installation

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
