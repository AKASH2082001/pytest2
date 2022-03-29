import Divisibliity

import pytest

def test_Div5():
    x=12
    result = Divisibliity.div_5(x)
    assert result == False

def test_Div7():
    x=70
    result = Divisibliity.div_7(x)
    assert result == True

def test_Div9():
    x=90
    result = Divisibliity.div_9(x)
    assert result == (x%9 == 0)

def test_Div10():
    x=3
    result = Divisibliity.div_10(x)
    assert result == False
