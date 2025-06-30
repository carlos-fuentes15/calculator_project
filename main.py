from calculator import Calculator
from calculator.calculations import Calculations
from calculator.logger import setup_logger


logger = setup_logger()

def repl():
    print("Welcome to the Advanced Calculator!")
    print("Commands: Add, Subtract, Multiply, Divide, History, Clear, Exit")

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
            else:
                tokens = user_input.split()
                if len(tokens) != 3:
                    logger.warning("Invalid command format.")
                    print("Usage: <operation> <num1> <num2>")
                    continue

                operation, a, b = tokens
                a, b = Decimal(a), Decimal(b)

                result = None
                if operation == "add":
                    result = Calculator.add(a, b)
                elif operation == "subtract":
                    result = Calculator.subtract(a, b)
                elif operation == "multiply":
                    result = Calculator.multiply(a, b)
                elif operation == "divide":
                    result = Calculator.divide(a, b)
                else:
                    logger.error("Unknown operation: %s", operation)
                    print("Unknown operation.")
                    continue

                logger.info("Result of %s: %s", operation, result)
                print(f" Result: {result}")
        except Exception as e:
            logger.exception("Unhandled error occurred")
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()

