"""Provides a plugin command for squaring a number."""

def register():
    """Register the square plugin command."""
    return {"square": square}

def square(x):
    """Return the square of a number."""
    return float(x) * float(x)
