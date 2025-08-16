# Learning About Dictionary
# Like Java Map

# Creation
# Decleration
from typing import Any


data = {"Hello" : 1, "Hi" : 2}

# Constructor
data = dict(Hello = 1, Hi = 2)

# Constructor with list of Tuple
data1 = dict([
    (1 , "One"),
    (2 , "Two"),
])

# Constructor with tuple of Tuple
data1 = dict((
    (1 , "One"),
    (2 , "Two"),
))

def get_keys(args:dict[str, Any]) -> set[str]:
    return set(args.keys())

def get_values(args:dict[str, Any]) -> list[Any]:
    return list(args.values())

def remove(src:dict[str, Any], *args:str) -> dict[str, Any]:
    copied = src.copy()
    for arg in args:
        del copied[arg] 
    return copied