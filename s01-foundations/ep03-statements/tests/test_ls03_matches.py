from operator import ge
from src.ls01_conditionals import Color
from src.ls03_matches import Book, Magazine, get_information, get_message_for_point, show_message_for_light


def test_show_message_for_light(capsys):
    show_message_for_light(Color.GREEN)
    stdout = capsys.readouterr()
    assert stdout.out.strip() == "Go"

    show_message_for_light(Color.RED)
    stdout = capsys.readouterr()
    assert stdout.out.strip() == "Stop"

    show_message_for_light(Color.YELLOW)
    stdout = capsys.readouterr()
    assert stdout.out.strip() == "Caution"

def test_get_message_for_point():
    assert get_message_for_point((0, 0)) == 'Origin'
    assert get_message_for_point((5, 0)) == 'X-axis at 5'
    assert get_message_for_point((0, 5)) == 'Y-axis at 5'
    assert get_message_for_point((-5, -5)) == 'Point at (-5, -5)'

def test_get_information():
    assert get_information(Book("Withering Heights")) == "Book: Withering Heights"
    assert get_information(Magazine("Time")) == "Magazine: Time"