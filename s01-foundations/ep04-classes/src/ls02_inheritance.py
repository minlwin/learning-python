from src.ls01_normal_classes import Car


class OffroadCar(Car):
    def __init__(self, brand: str, model: str, year: int) -> None:
        super().__init__(brand, model, year)
        self.type = "Offroad"

    def drive(self) -> None:
        return super().drive()
    
    def drive_offroad(self) -> None:
        print("Driving So hard")

    def get_info(self) -> str:
        return f"{self.type} {super().get_info()}"