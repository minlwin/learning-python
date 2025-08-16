from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand:str, model:str, year:int) -> None:
        super().__init__()
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def get_info(self) -> str:
        pass

class MotorCycle(Vehicle):
    def __init__(self, brand: str, model: str, year: int) -> None:
        super().__init__(brand, model, year)

    def drive(self) -> None:
        print(f"Riding {self.year} {self.brand} {self.model}.")
    
    def get_info(self) -> str:
        return f"{self.year} {self.brand} {self.model}"