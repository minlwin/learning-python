from src.ls05_tuples import filtering_tuple, mapping_tuple, pushing_tuple, reducing_tuple, removing_tuple, slicing_tuple, summing_tuple

def test_pushing_tuple():
    result = pushing_tuple(tuple(list(range(1, 4))), 4)
    assert result == (1, 2, 3, 4)

def test_removing_tuple():
    result = removing_tuple(tuple(list(range(1, 6))), 2, 3)
    assert (1, 2, 4, 5) == result

def test_slicing_tuple():
    result = slicing_tuple(tuple(list(range(1, 6))), 2,3)
    assert (3,) == result

def test_filtering_tuple():
    result = filtering_tuple(tuple(list(range(1, 10))), lambda a : a % 2 == 0)
    assert (2, 4, 6, 8) == result

def test_mapping_tuple():
    result = mapping_tuple(tuple(list(range(1, 4))), lambda a : str(a * 2))
    assert ("2", "4", "6") == result

def test_reducing_tuple():
    result = reducing_tuple(tuple(list(range(1, 4))), lambda a, b : a + b)
    assert 6 == result

def test_summing_tuple():
    result = summing_tuple(tuple(list(range(1, 4))))
    assert 6 == result