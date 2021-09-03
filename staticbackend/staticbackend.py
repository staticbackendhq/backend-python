"""StaticBackend class."""

from .config import Config


class StaticBackend(object):
    """
    StaticBackend is the base class for all staticbackend operations.
    """

    def __init__(self, config: Config):
        """
        Initializes the StaticBackend class.

        :param kwargs:
        config: Configure for StaticBackend client.
        """
        self.api_key = config.api_token
        self.endpoint = config.endpoint
