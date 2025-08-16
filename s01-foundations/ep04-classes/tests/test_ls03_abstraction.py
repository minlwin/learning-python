from src.ls03_abstraction import MotorCycle

def test_motorcycle_drive(capsys):
    ryolal_enfield = MotorCycle(brand="Royal Enfield", model="Classic 350", year=2023)
    ryolal_enfield.drive()

    captured = capsys.readouterr()
    assert captured.out == "Riding 2023 Royal Enfield Classic 350.\n"

def test_motorcycle_get_info():
    ryolal_enfield = MotorCycle(brand="Royal Enfield", model="Classic 350", year=2023)
    assert ryolal_enfield.get_info() == "2023 Royal Enfield Classic 350"