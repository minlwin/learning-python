from src.ls07_dicts import get_keys, get_values, remove


def test_get_keys():
    assert {"1", "2"} == get_keys({"1" : 1, "2" : 2})

def test_get_values():
    assert [1, 2] == get_values({"1" : 1, "2" : 2})

def test_remove():
    languages = {
        "1" : "Java",
        "2" : "JavaScript",
        "3" : "Kotlin",
        "4" : "TypeScript",
        "5" : "Dart",
        "6" : "Python",
    }

    assert {
        "1" : "Java",
        "2" : "JavaScript",
        "4" : "TypeScript",
        "6" : "Python",
    } == remove(languages, "3", "5")