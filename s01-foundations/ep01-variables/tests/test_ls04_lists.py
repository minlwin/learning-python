from src.ls04_lists import *

def test_appending_list():
    result = appending_list([1, 2, 3], 4)
    assert [1, 2, 3, 4] == result

def test_removing_list():
    result = removing_from_list(list(range(1, 10)), 3, 5)
    assert [1, 2, 3, 6, 7, 8, 9] == result

def test_slicing_list():
    result = slicing_list(list(range(1, 10)), 3, 5)
    assert [4, 5] == result

def test_filtering_list():
    result = filtering_list(list(range(1, 10)), lambda a : a % 2 == 0)
    assert [2, 4, 6, 8] == result

def test_mapping_list():
    result = mapping_list(["Java", "JavaScript", "TypeScript", "Dart", "Python"])
    assert [
        IndexAndValue(0, "Java"),
        IndexAndValue(1, "JavaScript"),
        IndexAndValue(2, "TypeScript"),
        IndexAndValue(3, "Dart"),
        IndexAndValue(4, "Python"),
    ] == result

def test_reducing_list():
    result = reducing_list(list(range(1, 10)), lambda a, b : a + b)
    assert 45 == result