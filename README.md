 HEAD

# Calculator Project
Overview:
This is a Python based calculator application developed with skills learned overtime across multiple assignments. This demonstrates the application design pattersn, environment based configuration, plugin systems, logging, and history tracking using Pandas. The calculator is used via a REPL interface.


## Setup Instructions
1. Clone the repository:
   git clone git@github.com:your-username/calculatorproject.git
   cd calculatorproject
2. Create and Activate a virual envrionment
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
3. Install the dependencies
   pip install -r requirements.txt
4. Create a .env file
   LOGLEVEL=INFO
   LOGFILE=app.log

## Running the Calculator
  Start the REPL by running:
  python main.py
Available commands include (EXAMPLES):
add 5 3
subtract 10 4
multiply 2 6
divide 8 2
menu (lists all plugins)
square 5 (from plugin)
save / load / clear / delete (manage history)
exit

## Features
Arithmetic Operations
Core arithmetic functions: Add, Subtract, Multiply, Divide.

Plugin System
Dynamically loads plugins from the calculator/plugins/ directory.
To list plugins, run menu in the REPL.

Calculation History with Pandas
History is tracked using Pandas and can be saved, loaded, cleared, or deleted.

Logging
Logging is managed through environment variables.
LOGLEVEL controls log severity.
LOGFILE specifies output file.
See logger.py.

## Environment Variables
Environment variables are loaded using dotenv and used to configure logging behavior.
Defined in .env:
 LOGLEVEL=INFO
 LOGFILE-app.log

## Design Patterns Used
Command Pattern
Used to map REPL commands to function calls in main.py. Each user command is encapsulated as an executable object.

Singleton Pattern
Used in the History class to ensure only one history tracker is used throughout the app.

## Exception Handling
LBYL (Look Before You Leap)
In main.py, user input is checked before execution:
  if len(args) < 2:
    print("Missing operands")

EAFP (Easier to Ask for Forgiveness)
In pluginloader.py, plugin loading uses try/except:
  try:
    module = importlib.importmodule(name)
except Exception:
    continue

## GitHub Actions CL
All tests are run via GitHub Actions on each push to main. See .github/workflows/python-app.yml.

## Video
: https://www.youtube.com/watch?v=vhYNu4j1Abg

## Testing and Coverage
Run tests: pytest --cov=calculator
Achieved 91%+ coverage.
Pylint checks are enforced via CI.

=======
# Calculator Project
Overview:
This is a Python based calculator application developed with skills learned overtime across multiple assignments. This demonstrates the application design pattersn, environment based configuration, plugin systems, logging, and history tracking using Pandas. The calculator is used via a REPL interface.


## Setup Instructions
1. Clone the repository:
   git clone git@github.com:your-username/calculator_project.git
   cd calculator_project
2. Create and Activate a virual envrionment
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
3. Install the dependencies
   pip install -r requirements.txt
4. Create a .env file
   LOG_LEVEL=INFO
   LOG_FILE=app.log

## Running the Calculator
  Start the REPL by running:
  python main.py
Available commands include (EXAMPLES):
add 5 3
subtract 10 4
multiply 2 6
divide 8 2
menu (lists all plugins)
square 5 (from plugin)
save / load / clear / delete (manage history)
exit

## Features
Arithmetic Operations
Core arithmetic functions: Add, Subtract, Multiply, Divide.

Plugin System
Dynamically loads plugins from the calculator/plugins/ directory.
To list plugins, run menu in the REPL.

Calculation History with Pandas
History is tracked using Pandas and can be saved, loaded, cleared, or deleted.

Logging
Logging is managed through environment variables.
LOG_LEVEL controls log severity.
LOG_FILE specifies output file.
See logger.py.

## Environment Variables
Environment variables are loaded using dotenv and used to configure logging behavior.
Defined in .env:
 LOG_LEVEL=INFO
 LOG_FILE-app.log

## Design Patterns Used
Command Pattern
Used to map REPL commands to function calls in main.py. Each user command is encapsulated as an executable object.

Singleton Pattern
Used in the History class to ensure only one history tracker is used throughout the app.

## Exception Handling
LBYL (Look Before You Leap)
In main.py, user input is checked before execution:
  if len(args) < 2:
    print("Missing operands")

EAFP (Easier to Ask for Forgiveness)
In plugin_loader.py, plugin loading uses try/except:
  try:
    module = importlib.import_module(name)
except Exception:
    continue

## GitHub Actions CL
All tests are run via GitHub Actions on each push to main. See .github/workflows/python-app.yml.

## Video
: https://www.youtube.com/watch?v=vhYNu4j1Abg

## Testing and Coverage
Run tests: pytest --cov=calculator
Achieved 91%+ coverage.
Pylint checks are enforced via CI.
>>>>>>> d0cedd9 (Update README.md)
