# log-decorator.py

# Task 1: Writing and Testing a Decorator

import logging
from functools import wraps

# one-time setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Logging function name
        logger.info(f"function: {func.__name__}")

        # Logging positional arguments
        pos_args = list(args) if args else "none"
        logger.info(f"positional parameters: {pos_args}")

        # Logging keyword arguments
        kw_args = kwargs if kwargs else "none"
        logger.info(f"keyword parameters: {kw_args}")

        # Call the function
        result = func(*args, **kwargs)

        # Logging return value
        logger.info(f"return: {result}")
        return result
    return wrapper

# Task 1a: Function with no parameters and no return
@logger_decorator
def greet():
    print("Hello, World!")

# Task 1b: Function with variable number of positional arguments
@logger_decorator
def check_args(*args):
    return True

# Task 1c: Function with keyword arguments, returns logger_decorator
@logger_decorator
def keyword_args_only(**kwargs):
    return logger_decorator

# Mainline code to test the decorated functions
if __name__ == "__main__":
    greet()  
    check_args(1, 2, 3)  
    keyword_args_only(a=5, b=10)  
