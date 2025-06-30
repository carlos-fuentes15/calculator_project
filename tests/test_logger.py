"""Test the logger setup using subprocess."""
import os
import subprocess

def test_logger_logs_to_file(tmp_path):
    """Test logger writes to a file."""
    # Set up a temporary log file path
    test_log_file = tmp_path / "test_log.log"
    env = os.environ.copy()
    env["LOG_FILE"] = str(test_log_file)

    # Command to run a Python script that uses the logger
    code = (
        "from calculator.logger import get_logger; "
        "logger = get_logger(); "
        "logger.info('Logging test message')"
    )

    # Execute the logger code in subprocess
    subprocess.run(["python", "-c", code], env=env, check=True)

    # Assert log file exists and contains the message
    assert test_log_file.exists()
    content = test_log_file.read_text()
    assert "Logging test message" in content
