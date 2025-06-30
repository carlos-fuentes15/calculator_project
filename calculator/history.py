"""Manages the history of calculations."""


class History:
    """Class to store and manage calculation history."""

    history_list = []

    @staticmethod
    def add_calculation(calculation):
        """Add a calculation to the history."""
        History.history_list.append(calculation)

    @staticmethod
    def get_last_calculation():
        """Return the last calculation."""
        return History.history_list[-1] if History.history_list else None

    @staticmethod
    def clear_history():
        """Clear the history list."""
        History.history_list.clear()

    @staticmethod
    def count():
        """Return the number of stored calculations."""
        return len(History.history_list)
