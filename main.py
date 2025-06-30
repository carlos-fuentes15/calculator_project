from decimal import Decimal
from calculator import Calculator
from calculator.calculations import Calculations
from calculator.logger import setup_logger
from calculator.plugin_loader import load_plugins

logger = setup_logger()
plugin_commands = load_plugins()

def repl():
    print("Welcome to the Advanced Calculator!")
    print("Commands: add, subtract, multiply, divide, history, clear, save, load, delete, menu, exit")

    while True:
        try:
            user_input = input(">>> ").strip().lower()
            logger.info("User input: %s", user_input)

            if user_input in ["exit", "quit"]:
                logger.info("Exiting application.")
                print("Goodbye.")
                break

            elif user_input == "history":
                logger.info("Fetching history.")
                for calc in Calculations.get_history():
                    print(calc)

            elif user_input == "clear":
                logger.info("Clearing history.")
                Calculations.clear_history()
                print("History cleared.")

            elif user_input == "menu":
                print("Built-in commands: add, subtract, multiply, divide, history, clear, save, load, delete, exit")
                print("Plugin commands:", ", ".join(plugin_commands.keys()))

            else:
                tokens = user_input.split()
                if len(tokens) < 2:
                    logger.warning("Invalid command format.")
                    print("Usage: <command> <arg1> [arg2]")
                    continue

                command = tokens[0]
                args = tokens[1:]

                if command in ["add", "subtract", "multiply", "divide"]:
                    if len(args) != 2:
                        print("Usage: <operation> <num1> <num2>")
                        continue

                    a, b = Decimal(args[0]), Decimal(args[1])

                    if command == "add":
                        result = Calculator.add(a, b)
                    elif command == "subtract":
                        result = Calculator.subtract(a, b)
                    elif command == "multiply":
                        result = Calculator.multiply(a, b)
                    elif command == "divide":
                        result = Calculator.divide(a, b)

                    logger.info("Result of %s: %s", command, result)
                    print(f"Result: {result}")

                elif command in plugin_commands:
                    try:
                        result = plugin_commands[command](*args)
                        logger.info("Plugin %s executed with result: %s", command, result)
                        print(f"Plugin Result: {result}")
                    except Exception as e:
                        logger.exception("Plugin command error")
                        print(f"Plugin Error: {e}")

                else:
                    logger.error("Unknown command: %s", command)
                    print("Unknown command. Try 'menu' to see available options.")

        except Exception as e:
            logger.exception("Unhandled error occurred")
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
