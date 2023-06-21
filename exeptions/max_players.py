"""Importing two libraries: `logging` and `wraps` from the `functools` module."""
import logging
from functools import wraps


class TooManyPlayersException(Exception):
    pass


def logged(exception, mode):
    """
       A decorator that logs exceptions raised in a function to a file or console.

       Args:
           exception (Exception): The exception to catch.
           mode (str): The mode to log the exceptions. Can be `file` or `console`.
       """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                class_name = args[0].__class__.__name__
                message = f"Exception {exception.__name__} was raised in {class_name}.{func.__name__} with message: {e}"
                if mode == "file":
                    logging.basicConfig(filename='exceptions.log', level=logging.ERROR)
                    logging.error(message)
                elif mode == "console":
                    logging.basicConfig(level=logging.ERROR)
                    logging.error(message)

        return wrapper

    return decorator
