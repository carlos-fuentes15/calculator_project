from calculator.calculation import Calculation

class Calculations:
    history = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        cls.history.append(calculation)

    @classmethod
    def last(cls) -> Calculation:
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear(cls) -> None:
        cls.history.clear()

    @classmethod
    def count(cls) -> int:
        return len(cls.history)
