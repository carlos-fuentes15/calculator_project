"""Logger setup for the calculator application."""
import logging
import os

# Default log file name or from environment variable
LOG_FILE = os.getenv("LOG_FILE", "calculator.log")

# Create and configure logger
logger = logging.getLogger("calculator_logger")
logger.setLevel(logging.INFO)

# Prevent adding multiple handlers during tests or reloads
if not logger.handlers:
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def get_logger():
    """Return the configured logger."""
    return logger
