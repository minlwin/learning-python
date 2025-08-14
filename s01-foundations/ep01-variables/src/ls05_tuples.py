# Learning About Tuple
# Tuple is Immutable Sequence

# Creating Turples
# Declaration
from functools import reduce
from typing import Callable


jdc = ("Learning Java", "Sometimes React", "Maybe Python")

# Using Constructor
jdc = tuple([1, 2, 3])

# Tuple is Immutable Collection, It's elements can't change
# But We can Create new tuple from existing tuple

def pushing_tuple(args:tuple[int, ...], element:int) -> tuple[int, ...]:
    _list = list(args)
    _list.append(element)
    return tuple(_list)

def removing_tuple(args:tuple[int, ...], start: int, end: int) -> tuple[int, ...]:
    _list = list(args)
    _list[start : end] = []
    return tuple(_list)

def slicing_tuple(args:tuple[int, ...], start: int, end: int) -> tuple[int, ...]:
    _list = list(args)
    return tuple(_list[start : end])

def filtering_tuple(args:tuple[int, ...], func:Callable[[int], int]) -> tuple[int, ...]:
    return tuple(filter(func, args))

def mapping_tuple(args:tuple[int, ...], func:Callable[[int], str]) -> tuple[str, ...]:
    return tuple(map(func, args))

def reducing_tuple(args:tuple[int, ...], func:Callable[[int,int], int]) -> int:
    return reduce(func, args)

def summing_tuple(args:tuple[int, ...]) -> int:
    return reduce(lambda a, b : a + b, args)