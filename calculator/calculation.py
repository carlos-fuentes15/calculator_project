"""Handles creation and execution of a single calculation."""


class Calculation:
    """A mathematical calculation."""

    def __init__(self, a: float, b: float, operation):
        """Initialize a Calculation instance."""
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self):
        """Stored operation."""
        return self.operation(self.a, self.b)

    def __str__(self):
        """Return a string representation of the calculation."""
        op_symbol = {
            'add': '+',
            'subtract': '-',
            'multiply': '*',
            'divide': '/'
        }.get(self.operation.__name__, '?')
        return f"{self.a} {op_symbol} {self.b} = {self.perform()}"

    @staticmethod
    def create(a, b, operation):
        """Create a Calculation instance."""
        return Calculation(a, b, operation)
