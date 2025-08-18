from enum import Enum
from functools import wraps

class DecorateAt(Enum):
    BEFORE = 1
    AFTER = 2
    FALLING = 3

def interceptor(at: DecorateAt):
    def wrapper(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            try:
                if at == DecorateAt.BEFORE:
                    print("Something is happening before the function is called.")
                result = func(*args, **kwargs)
                if at == DecorateAt.AFTER:
                    print("Something is happening after the function is called.")
            except Exception as e:
                if at == DecorateAt.FALLING:
                    print("Something went wrong:", e)
                raise
            return result
        return decorator
    return wrapper

@interceptor(at=DecorateAt.BEFORE)
def my_function():
    print("The function is called.")

if __name__ == "__main__":
    my_function()