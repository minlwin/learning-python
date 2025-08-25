from src.ls01_get_type import get_type

def test_get_type() :
    result = get_type(False)
    assert result == 'bool'

    result = get_type("Hello Python")
    assert result == 'str'

    result = get_type(100)
    assert result == 'int'

    result = get_type(10.4)
    assert result == 'float'

    result = get_type(10 + 3j)
    assert result == "complex"
    
    result = get_type([10, 2, 1])
    assert result == 'list'

    result = get_type((1, "Hello"))
    assert result == 'tuple'

    result = get_type(range(6, 2))
    assert result == 'range'

    result = get_type({1, 2, 3, 4, "Hello"})
    assert result == 'set'

    result = get_type({"language" : "Python", "level" : "Helloworld"})
    assert result == "dict"