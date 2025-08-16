from dataclasses import dataclass
from typing import Any
from src.ls01_conditionals import Color


def show_message_for_light(color:Color) -> None:
    match(color):
        case Color.RED:
            print("Stop")
        case Color.YELLOW:
            print("Caution")
        case Color.GREEN:
            print("Go")

def get_message_for_point(point:tuple[int, int]) -> str:
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"X-axis at {x}"
        case (0, y):
            return f"Y-axis at {y}"
        case (x, y):
            return f"Point at ({x}, {y})"
        case _:
            return "Unknown point"
        
@dataclass(frozen=True)
class Book():
    title:str

@dataclass(frozen=True)
class Magazine():
    title:str

def get_information(item:Any) -> str:
    match(item):
        case Book(title):
            return f"Book: {title}"
        case Magazine(title):
            return f"Magazine: {title}"
        case _:
            return "Unknown item"