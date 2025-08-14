from src.ls03_default_values import with_devault_value, witn_mixing_default_value

def test_with_devault_value():
    assert "No Name0" == with_devault_value()
    assert "No Name10" == with_devault_value(value=10)
    assert "Hello0" == with_devault_value(name="Hello")
    assert "Levi's501" == with_devault_value("Levi's", 501)
    assert "Levi's511" == with_devault_value(value=511, name="Levi's")  

def test_witn_mixing_default_value():
    assert "Hello Python" == witn_mixing_default_value("Hello")
    assert "Hi Python" == witn_mixing_default_value(first= "Hi")
    assert "Hello Java" == witn_mixing_default_value("Hello", "Java")
    assert "Hi Java" == witn_mixing_default_value(second = "Java", first = "Hi")
