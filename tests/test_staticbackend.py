import unittest

from staticbackend import StaticBackend, Config


class TestStaticBackend(unittest.TestCase):
    def test_login(self):
        conf = Config(api_token="123456", endpoint="https://na1.staticbackend.com")
        backend = StaticBackend(conf)
        backend.login("test", "test")
        self.assertTrue(backend.is_logged_in())
