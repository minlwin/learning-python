from src.ls08_stacks import is_symmetric

def test_empty():
    assert not is_symmetric('')

def test_other_values():
    assert not is_symmetric('(a)')

def test_success():
    assert is_symmetric("()[]{}<>")
    assert is_symmetric("([<{}>])")
    assert is_symmetric("([])<>{}")

def test_not_success():
    assert not is_symmetric("()[]}<>")
    assert not is_symmetric("([<{}>][)")
    assert not is_symmetric("([])>{}")
