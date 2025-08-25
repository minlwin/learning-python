from pydantic import ValidationInfo

def not_blank(value: str, info:ValidationInfo) -> str:
    if value.strip() == '':
        raise ValueError(f"{info.field_name or 'Field'} is required.")
    return value.strip()
