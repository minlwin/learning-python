from enum import Enum

class Status(Enum):
    NEW = (1, "New Item")
    IN_PROGRESS = (2, "In Progress")
    DONE = (3, "Done")

    def __init__(self, code:int, description:str) -> None:
        super().__init__()
        self.code = code
        self.description = description

    def is_done(self) -> bool:
        return self == Status.DONE