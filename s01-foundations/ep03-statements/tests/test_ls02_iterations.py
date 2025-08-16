from src.ls02_iterations import fibo, is_prime


def test_fibo():
    assert fibo(0) == [0]
    assert fibo(5) == [0, 1, 1, 2, 3, 5]

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True