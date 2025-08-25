from pydantic import BaseModel, ValidationError, ValidationInfo, field_validator

from src._validators import not_blank

class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    @field_validator('title', mode='after')
    @classmethod
    def validate_title(cls, value: str, info: ValidationInfo) -> str:
        return not_blank(value, info)
    
if __name__ == "__main__":
    try:
        data = {"id": 1, "title": "", "description" : "", "complete": False}
        Task(**data)
    except ValidationError as e:
        print(e.errors())