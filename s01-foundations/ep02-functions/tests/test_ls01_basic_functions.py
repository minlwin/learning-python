from src.ls01_basic_functions import add, twice


def test_single_args_function():
    assert 20 == twice(10)

def test_multiple_args_function():
    assert 10 == add(3, 7)

def test_with_named_parameter():
    assert 10 == add(second=4, first=6)