from src.ls06_enum_classes import Status


def test_status_enum():
    assert Status.NEW.code == 1
    assert Status.NEW.description == "New Item"
    assert Status.IN_PROGRESS.code == 2
    assert Status.IN_PROGRESS.description == "In Progress"
    assert Status.DONE.code == 3
    assert Status.DONE.description == "Done"

def test_status_is_done():
    assert Status.NEW.is_done() is False
    assert Status.IN_PROGRESS.is_done() is False
    assert Status.DONE.is_done() is True
