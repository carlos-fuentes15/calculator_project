"""Unit tests for the History class in calculator.history."""

from calculator.history import History


class DummyCalculation:  # pylint: disable=too-few-public-methods
    """Dummy object to simulate calculation."""
    def __init__(self, result):
        self.result = result

def test_add_calculation():
    """Test adding a calculation to history."""
    History.clear_history()
    calc = DummyCalculation(10)
    History.add_calculation(calc)
    assert History.count() == 1
    assert History.get_last_calculation() == calc


def test_get_last_calculation_when_empty():
    """Test get_last_calculation when history is empty."""
    History.clear_history()
    assert History.get_last_calculation() is None


def test_clear_history():
    """Test clearing the history."""
    History.add_calculation(DummyCalculation(5))
    History.clear_history()
    assert History.count() == 0
