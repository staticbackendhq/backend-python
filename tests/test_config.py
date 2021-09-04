import unittest

from staticbackend.errors import ValidationError

from staticbackend.config import Config


class TestStringMethods(unittest.TestCase):
    def test_invalid_endpoint(self) -> None:
        with self.assertRaises(ValidationError):
            Config(api_token="foo", endpoint="bar")

    def test_invalid_api_token(self) -> None:
        with self.assertRaises(ValidationError):
            Config(endpoint="http://127.0.0.1:8099")

        with self.assertRaises(ValidationError):
            Config(api_token="", endpoint="http://127.0.0.1:8099")

    def test_normal(self) -> None:
        try:
            Config(api_token="foo", endpoint="http://127.0.0.1:8099")
        except ValidationError:
            self.fail("Config should not raise an error.")
