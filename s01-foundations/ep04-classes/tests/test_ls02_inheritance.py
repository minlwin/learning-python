from src.ls02_inheritance import OffroadCar

def test_offroad_car_drive(capsys):
    pajero = OffroadCar(brand="Mitsubishi", model="Pajero", year=2025)
    pajero.drive()

    captured = capsys.readouterr()
    assert captured.out == "Driving 2025 Mitsubishi Pajero.\n"

def test_offroad_car_get_info():
    pajero = OffroadCar(brand="Mitsubishi", model="Pajero", year=2025)
    assert "Offroad 2025 Mitsubishi Pajero" == pajero.get_info()