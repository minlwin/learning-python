from src.ls01_normal_classes import Car

def test_car_drive(capsys):
    honda_civic = Car(brand="Honda", model="Civic", year=2025)
    honda_civic.drive()

    captured = capsys.readouterr()
    assert captured.out == "Driving 2025 Honda Civic.\n"

def test_car_get_info():
    honda_civic = Car(brand= "Honda", model= "Civic", year=2025)
    assert "2025 Honda Civic" == honda_civic.get_info()