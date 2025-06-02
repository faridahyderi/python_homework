# type-decorator.py

# Task 2: A Decorator that Takes an Argument

def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

# Function that returns an integer 5, but is decorated to convert return to string
@type_converter(str)
def return_int():
    return 5

# Function that returns a string "not a number", decorated to convert return to int
@type_converter(int)
def return_string():
    return "not a number"

# Mainline code
if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)  # Expected output: str

    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!")  # Expected output
