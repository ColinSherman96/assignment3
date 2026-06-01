import pytest
from app.operations import addition, subtraction, multiplication, division

def test_addition():
    assert addition(1, 1) == 2
    
def test_subtraction():
    assert subtraction(1, 1) == 0

def test_multiplication():
    assert multiplication(2, 3) == 6

def test_division_positive():
    assert division(6, 3) == 2

def test_division_negative():
    with pytest.raises(ValueError):
        division(1, 0)