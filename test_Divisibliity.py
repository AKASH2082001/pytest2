import Divisibliity

import pytest

def test_Div5():
    x=50
    result = Divisibliity.div_5(x)
    assert result == (x%5 == 0)

def test_Div7():
    x=70
    result = Divisibliity.div_7(x)
    assert result == (x%7 == 0)

def test_Div9():
    x=90
    result = Divisibliity.div_9(x)
    assert result == (x%9 == 0)

def test_Div10():
    x=100
    result = Divisibliity.div_10(x)
    assert result == (x%10 == 0)
