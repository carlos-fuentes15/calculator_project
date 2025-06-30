"""Unit tests for the Calculation class and operations."""

from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


def test_perform_add():
    """Test that addition works correctly."""
    c = Calculation(3, 2, add)
    assert c.perform() == 5


def test_perform_subtract():
    """Test that subtraction works correctly."""
    c = Calculation(3, 2, subtract)
    assert c.perform() == 1


def test_perform_multiply():
    """Test that multiplication works correctly."""
    c = Calculation(3, 2, multiply)
    assert c.perform() == 6


def test_perform_divide():
    """Test that division works correctly."""
    c = Calculation(10, 2, divide)
    assert c.perform() == 5
