import Divisibliity

import pytest

@pytest.fixture()
def input():
    x=50
    return x

def test_Div5(input):
    result = Divisibliity.div_5(input)
    assert result == True

def test_Div7(input):
    result = Divisibliity.div_7(input)
    assert result == False

def test_Div9(input):
    result = Divisibliity.div_9(input)
    assert result == False

def test_Div10(input):
    result = Divisibliity.div_10(input)
    assert result == True
