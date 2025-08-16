from typing import Final

BRACKETS:Final[tuple[tuple[str, str], ...]] = (
    ('(', ')'), 
    ('<', '>'), 
    ('{', '}'), 
    ('[', ']')
)

def is_symmetric(value:str) -> bool:
    
    if not value or not value.strip():
        return False

    stack:list[str] = []

    open_brackets:set[str] = {pair[0] for pair in BRACKETS}
    close_to_open:dict[str, str] = {pair[1] : pair[0] for pair in BRACKETS}
    
    for char in value:
        if char in open_brackets:
            stack.append(char)
        else:
            if not stack or stack.pop() != close_to_open.get(char, ""):  
                return False
        
    return not stack