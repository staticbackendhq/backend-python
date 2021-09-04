import unittest

from pydantic import ValidationError
from staticbackend import Config, StaticBackend


class TestStaticBackend(unittest.TestCase):
    def test_login(self) -> None:
        conf = Config(api_token="foobar", endpoint="https://na1.staticbackend.com")
        backend = StaticBackend(conf)

        # validate email address.
        with self.assertRaises(ValidationError):
            backend.login("foo", "bar")  # type: ignore

        try:
            backend.login("foo@bar.com", "foobar")  # type: ignore
        except ValidationError:
            self.fail("Email validate should not raise an error.")
