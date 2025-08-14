from functools import reduce

def concat(*args:str) -> str:
    return reduce(lambda a, b : a + b, args)

def joining(*args:str) -> str:
    return " ".join(args)

def formatting(template:str, *args) -> str:
    return template.format(*args)

def times_string(value:str, time:int) -> str:
    return value * time 