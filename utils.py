import logging
import sys

experiment_state = {}


def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            logger.error(e)
            logger.exception(f"Exception occurred in function: {func.__name__}")
            print("do post processing...")

    return inner_function


class Logger:
    def __new__(cls, *args, **kwargs):
        _logger = logging.getLogger()
        _logger.setLevel(logging.DEBUG)
        stdout_handler = logging.StreamHandler(sys.stdout)
        stderr_handler = logging.StreamHandler(sys.stderr)
        stdout_handler.setLevel(logging.INFO)
        stderr_handler.setLevel(logging.WARNING)
        formatter = logging.Formatter(
            fmt='%(asctime)s %(levelname)s: %(message)s',
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        stdout_handler.setFormatter(formatter)
        stderr_handler.setFormatter(formatter)
        _logger.addHandler(stdout_handler)
        _logger.addHandler(stderr_handler)
        return _logger


logger = Logger()
