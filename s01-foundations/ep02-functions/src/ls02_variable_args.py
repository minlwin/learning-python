def with_variable_args(name: str, *args:int)  -> int:
    print(name)
    return sum(args)

def with_variable_args_first(*args: int, name:str) -> int:
    print(name)
    return sum(args)
