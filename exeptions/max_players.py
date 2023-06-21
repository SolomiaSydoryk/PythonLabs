"""Importing two libraries: `logging` and `wraps` from the `functools` module."""
import logging
from functools import wraps


class TooManyPlayersException(Exception):
    """Class for my exceptions"""

    def __str__(self):
        return "Maximum number of players already reached."


def logged(exception_type, mode):
    """
       A decorator that logs exceptions raised in a function to a file or console.

       Args:
           exception_type (Exception): The exception to catch.
           mode (str): The mode to log the exceptions. Can be `file` or `console`.
       """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_type as exc:
                class_name = args[0].__class__.__name__
                message = f"Exception {exception_type.__name__} was raised in {class_name}.{func.__name__} with " \
                          f" message: {exc}"
                if mode == "file":
                    logging.basicConfig(filename='exceptions.log', level=logging.WARNING, filemode="w")
                    logging.warning(message)
                elif mode == "console":
                    logging.basicConfig(level=logging.WARNING)
                    logging.warning(message)
                else:
                    raise ValueError("You are invalid") from exc
                return TooManyPlayersException

        return wrapper

    return decorator
