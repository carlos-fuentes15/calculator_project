"""Main entry point for the advanced calculator REPL."""
from decimal import Decimal, InvalidOperation
from calculator import Calculator
from calculator.calculations import Calculations
from calculator.logger import get_logger
from calculator.plugin_loader import load_plugins

logger = get_logger()

# Load plugins and store commands in a single dictionary
plugin_commands = {}
for plugin in load_plugins():
    plugin_commands.update(plugin.register())


def show_menu():
    """Display standard commands and plugin command list."""
    print("Built-in commands: add, subtract, multiply, divide, history, clear, save, "
          "load, delete, menu, exit")
    print("Plugin commands:", ", ".join(plugin_commands.keys()))


def parse_args(args):
    """Convert string arguments to Decimal if possible."""
    if len(args) != 2:
        raise ValueError("Usage: <operation> <num1> <num2>")
    try:
        return Decimal(args[0]), Decimal(args[1])
    except InvalidOperation as e:
        raise ValueError("Invalid number format") from e


def handle_builtin_operation(command, args):
    """Perform standard calculator operations."""
    a, b = parse_args(args)

    if command == "add":
        return Calculator.add(a, b)
    if command == "subtract":
        return Calculator.subtract(a, b)
    if command == "multiply":
        return Calculator.multiply(a, b)
    if command == "divide":
        return Calculator.divide(a, b)

    raise ValueError(f"Unknown operation: {command}")


def handle_plugin_command(command, args):
    """Execute a plugin command."""
    try:
        decimal_args = [Decimal(arg) for arg in args]
        return plugin_commands[command](*decimal_args)
    except (TypeError, ValueError, KeyError) as e:
        raise RuntimeError(f"Plugin error: {e}") from e


def repl():
    """Run the calculator's REPL loop."""
    print("Welcome to the Advanced Calculator!")
    print("Commands: add, subtract, multiply, divide, history, clear, menu, exit")

    while True:
        user_input = input(">>> ").strip().lower()
        logger.info("User input: %s", user_input)

        if user_input in ["exit", "quit"]:
            logger.info("Exiting application.")
            print("Goodbye.")
            break

        if user_input == "menu":
            show_menu()
            continue

        if user_input == "history":
            logger.info("Fetching history.")
            for calc in Calculations.get_history():
                print(calc)
            continue

        if user_input == "clear":
            logger.info("Clearing history.")
            Calculations.clear_history()
            print("History cleared.")
            continue

        tokens = user_input.split()
        if not tokens:
            print("No input detected.")
            continue

        command, *args = tokens

        try:
            if command in ["add", "subtract", "multiply", "divide"]:
                result = handle_builtin_operation(command, args)
                print(f"Result: {result}")
                logger.info("Result of %s: %s", command, result)
            elif command in plugin_commands:
                result = handle_plugin_command(command, args)
                print(f"Plugin Result: {result}")
                logger.info("Plugin %s executed with result: %s", command, result)
            else:
                logger.warning("Unknown command: %s", command)
                print("Unknown command. Try 'menu' to see available options.")
        except (ValueError, ZeroDivisionError, RuntimeError) as e:
            logger.error("Error occurred: %s", e)
            print(f"Error: {e}")


if __name__ == "__main__":
    repl()
