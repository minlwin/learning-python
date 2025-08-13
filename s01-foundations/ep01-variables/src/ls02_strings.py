from functools import reduce

def concat(*args:str) -> str:
    return reduce(lambda a, b : a + b, args)

def joining(*args:str) -> str:
    return " ".join(args)

def format(template:str, args:map) -> str:
    return template.format(args)

