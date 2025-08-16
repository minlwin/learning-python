from abc import ABC, abstractmethod, abstractmethod

class Vehicle(ABC):
    class Engine:
        def __init__(self, horsepower: int) -> None:
            self.horsepower = horsepower

        def start(self) -> None:
            print(f"Engine with {self.horsepower} HP started.")
    
    def __init__(self, brand: str, model: str, year: int, engine_hp: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = self.Engine(engine_hp)

    @abstractmethod
    def drive(self) -> None:
        pass

    @abstractmethod
    def get_info(self) -> str:
        pass

class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, engine_hp: int) -> None:
        super().__init__(brand, model, year, engine_hp)

    def drive(self) -> None:
        print(f"Driving {self.year} {self.brand} {self.model}.")
        self.engine.start()

    def get_info(self) -> str:
        return f"{self.year} {self.brand} {self.model} with {self.engine.horsepower} HP."
