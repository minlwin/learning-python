from src.ls02_strings import concat, formatting, joining, times_string


def test_concat():
    assert "Python" == concat("Py", "thon")
    assert "Hello Python" == concat("Hello", ' ', "Python")


def test_joing():
    assert "Hello Python" == joining("Hello", "Python")

def test_format():
    assert "Hello Python" == formatting("Hello {}", "Python")

def test_times_string():
    assert "PythonPythonPython" == times_string("Python", 3)
