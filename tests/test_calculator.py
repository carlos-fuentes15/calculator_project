"""Unit tests for the Calculator class."""

import os
import sys
from decimal import Decimal
import pytest

# Ensure the calculator module can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import Calculator  # pylint: disable=wrong-import-position

def test_add():
    """Test addition operation."""
    assert Calculator.add(Decimal("2"), Decimal("3")) == Decimal("5")

def test_subtract():
    """Test subtraction operation."""
    assert Calculator.subtract(Decimal("5"), Decimal("2")) == Decimal("3")

def test_multiply():
    """Test multiplication operation."""
    assert Calculator.multiply(Decimal("4"), Decimal("2")) == Decimal("8")

def test_divide():
    """Test division operation."""
    assert Calculator.divide(Decimal("10"), Decimal("2")) == Decimal("5")

def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError):
        Calculator.divide(Decimal("5"), Decimal("0"))
