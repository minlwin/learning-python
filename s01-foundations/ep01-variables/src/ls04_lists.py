from dataclasses import dataclass
from functools import reduce
from typing import Callable, Generic, TypeVar

# Learning About List
# Create List

# Declaration
str_list:list[str] = ["Hello", "Python"]
# list constructor
int_list:list[int] = list((1, 2, 3))

T = TypeVar('T')

@dataclass
class IndexAndValue(Generic[T]):
    index:int
    value:T

def appending_list(data_list:list[int], *args:int) -> list[int] :
    result = data_list.copy()
    result.append(*args)
    return result

def removing_from_list(data_list:list[int], start:int, end:int) -> list[int]:
    result = data_list.copy()
    result[start : end] = []
    return result

def slicing_list(args:list[int], start:int, end:int) -> list[int]:
    return args[start: end]

def filtering_list(data_list:list[int], func: Callable[[int], bool]) ->list[int]:
    return list(filter(func, data_list))

def mapping_list(args:list[str]) -> list[IndexAndValue[str]] :
    return list(map(lambda x : IndexAndValue[str](x[0], x[1]), enumerate(args)))

def reducing_list(data_list:list, func:Callable[[int, int], int]) -> int:
    return reduce(func, data_list)
