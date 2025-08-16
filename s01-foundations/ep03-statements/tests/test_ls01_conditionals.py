from src.ls01_conditionals import Color, can_go_safily, get_color

def test_get_color():
    assert get_color("red") == Color.RED
    assert get_color("green") == Color.GREEN
    assert get_color("yellow") == Color.YELLOW
    assert not get_color("pink")

def test_can_go_safily():
    assert can_go_safily(Color.GREEN) is True
    assert can_go_safily(Color.YELLOW) is False
    assert can_go_safily(Color.RED) is False