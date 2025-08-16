class Car:
    def __init__(self, brand:str, model:str, year:int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self) -> None:
        print(f"Driving {self.year} {self.brand} {self.model}.")
    
    def get_info(self) -> str:
        return f"{self.year} {self.brand} {self.model}"

if __name__ == '__main__':
    honda_civic = Car("Honda", "Civic", 2025)
    honda_civic.drive()
