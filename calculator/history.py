"""Manages the history of calculations with file support using pandas."""

import os
import pandas as pd
from calculator.calculations import Calculations


class History:
    """Class to store and manage calculation history."""
    history_list = []
    history_file = os.getenv("HISTORY_FILE", "history.csv")

    @staticmethod
    def add_calculation(calculation):
        """Add a calculation to the history."""
        History.history_list.append(calculation)
        Calculations.add_calculation(calculation)  # Sync with Calculations

    @staticmethod
    def get_last_calculation():
        """Return the last calculation."""
        return History.history_list[-1] if History.history_list else None

    @staticmethod
    def clear_history():
        """Clear the history list."""
        History.history_list.clear()
        Calculations.clear_history()  # Sync clearing

    @staticmethod
    def count():
        """Return the number of stored calculations."""
        return len(History.history_list)

    @staticmethod
    def save_history():
        """Save the current history to a CSV file."""
        if not History.history_list:
            raise ValueError("No history to save.")
        df = pd.DataFrame([str(calc) for calc in History.history_list], columns=["calculation"])
        df.to_csv(History.history_file, index=False)

    @staticmethod
    def load_history():
        """Load history from the CSV file."""
        if not os.path.exists(History.history_file):
            raise FileNotFoundError("History file not found.")
        df = pd.read_csv(History.history_file)
        History.history_list = df["calculation"].tolist()
        Calculations.history = History.history_list  # Sync loaded list

    @staticmethod
    def delete_history_file():
        """Delete the saved history file."""
        if os.path.exists(History.history_file):
            os.remove(History.history_file)
            print("Deleted file:", History.history_file)  # Optional print
        else:
            raise FileNotFoundError("No history file to delete.")
        
