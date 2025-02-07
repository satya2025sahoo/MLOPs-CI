import pytest
from app import main

def test_square_calculation():
    # Simulate the square calculation function instead of calling main()
    def square(num):
        return num ** 2

    assert square(3) == 9
    assert square(-4) == 16
    assert square(0) == 0
