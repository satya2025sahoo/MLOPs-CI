import pytest
from app import main

def test_square_calculation():
    assert main(3) == 9
    assert main(-4) == 16
    assert main(0) == 0
