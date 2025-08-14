def with_keywords(**keywords) -> dict:
    return keywords

def keywords_with_var_args(*args:int, **keywords) -> tuple[int, dict]:
    return (sum(args), keywords)