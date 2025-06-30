"""Tests for square plugin."""
from calculator.plugins import square

def test_square_positive_number():
    """Test square of a positive number."""
    assert square.square(5) == 25

def test_square_negative_number():
    """Test square of a negative number."""
    assert square.square(-4) == 16

def test_square_zero():
    """Test square of zero."""
    assert square.square(0) == 0
