from src.ls03_numbers import *

def test_plus():
    assert 10 == plus(6, 4)

def test_minus():
    assert 2 == minus(6, 4)

def test_multiply():
    assert 24 == multiply(6, 4)

def test_divide():
    assert 1.5 == divide(3, 2)

def test_divide_as_int():
    assert 1 == divide_as_int(3, 2)

def test_exponent():
    assert 8 == exponent(2, 3)