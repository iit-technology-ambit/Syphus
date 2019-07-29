"""Collection of all error classes."""


class LoginError(Exception):
    """
    Raised when someone maliciously tries to enter some data without proper
    authentication.
    """
    pass
