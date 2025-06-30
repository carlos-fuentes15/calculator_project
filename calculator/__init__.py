"""Calculator module handling basic arithmetic operations with history tracking."""

from decimal import Decimal
from typing import Callable

from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from calculator.calculations import Calculations


class Calculator:
    """Does operations and logs them to history."""
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation:
    Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Addition."""
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Subtraction."""
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Multiplication."""
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Division."""
        return Calculator._perform_operation(a, b, divide)
