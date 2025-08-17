import datetime

class Car:
    def __init__(self, brand:str, model:str, year:int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self) -> None:
        print(f"Driving {self.year} {self.brand} {self.model}.")
    
    def get_info(self) -> str:
        return f"{self.year} {self.brand} {self.model}"
    
    @classmethod
    def get_latest_instance(cls, brand:str, model:str) -> 'Car':
        return cls(brand, model, datetime.datetime.now().year)

    @staticmethod
    def is_latest_model(car: 'Car') -> bool:
        return car.year == datetime.datetime.now().year

if __name__ == '__main__':
    honda_civic = Car("Honda", "Civic", 2025)
    honda_civic.drive()
