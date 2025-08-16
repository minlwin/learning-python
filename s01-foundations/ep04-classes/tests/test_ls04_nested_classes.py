from src.ls04_nested_classes import Car

def test_car_drive(capsys):
    honda_civic = Car(brand="Honda", model="Civic", year=2025, engine_hp=150)
    honda_civic.drive()

    captured = capsys.readouterr()
    assert captured.out == f"Driving 2025 Honda Civic.\nEngine with 150 HP started.\n"

def test_car_get_info():
    honda_civic = Car(brand="Honda", model="Civic", year=2025, engine_hp=150)
    assert honda_civic.get_info() == "2025 Honda Civic with 150 HP."