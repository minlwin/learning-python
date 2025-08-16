from dataclasses import dataclass
from enum import Enum

@dataclass
class ColorInfo:
    value: str
    status: str

class Color(Enum):
    RED = ColorInfo("red", "Stop")
    GREEN = ColorInfo("green", "Go")
    YELLOW = ColorInfo("yellow", "Wait")

def get_color(value:str) -> Color | None:
    for color in Color:
        if color.value.value == value:
            return color
    return None