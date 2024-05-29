import os
import pytest
from verbose_terminal import console

def test_log_verbose(capsys):
    console.log("Test log message")
    captured = capsys.readouterr()
    print(captured.out)
    assert "Test log message" in captured.out

def test_debug_verbose(capsys):
    console.debug("Test debug message")
    captured = capsys.readouterr()
    print(captured.out)
    assert "Test debug message" in captured.out

def test_info_verbose(capsys):
    console.info("Test info message")
    captured = capsys.readouterr()
    print(captured.out)
    assert "Test info message" in captured.out

def test_success_verbose(capsys):
    console.success("Test success message")
    captured = capsys.readouterr()
    print(captured.out)
    assert "Test success message" in captured.out

def test_warning_verbose(capsys):
    console.warning("Test warning message")
    captured = capsys.readouterr()
    print(captured.out)
    assert "Test warning message" in captured.out

def test_error_verbose(capsys):
    console.error("Test error message")
    captured = capsys.readouterr()
    print(captured.out)
    assert "Test error message" in captured.out

def test_critical_verbose(capsys):
    console.critical("Test critical message")
    captured = capsys.readouterr()
    print(captured.out)
    assert "Test critical message" in captured.out

def test_verbose_false(capsys):
    console.success("Test verbose false message", verbose=False)
    captured = capsys.readouterr()
    print(captured.out)
    assert "" in captured.out

def test_all_logs_level():
    log_file = 'test_logs.log'
    console.enable_logging(log_file=log_file, log_level='DEBUG')
    
    console.log("This is a test log message")
    console.success("This is a test success message")
    console.info("This is a test info message")
    console.debug("This is a test debug message")
    console.warning("This is a test warning message")
    console.error("This is a test error message")
    console.critical("This is a test critical message")
    
    logs = console.view_logs()
    
    assert "This is a test log message" in logs
    assert "This is a test success message" in logs
    assert "This is a test info message" in logs
    assert "This is a test debug message" in logs
    assert "This is a test warning message" in logs
    assert "This is a test error message" in logs
    assert "This is a test critical message" in logs
    console.clear_logs()

def test_view_logs_no_logging_enabled(capsys):
    console.disable_logging()
    console.view_logs()
    captured = capsys.readouterr()
    print(captured.out)
    assert "Logging is not enabled. No logs to clear." in captured.out

def test_view_logs(capsys):
    console.enable_logging('test_logs.log', 'DEBUG')
    console.debug("Debug message", verbose=True)
    console.info("Info message", verbose=True)
    logs = console.view_logs()
    assert "Debug message" in logs
    assert "Info message" in logs
    console.clear_logs()

def test_clear_logs_no_logging_enabled(capsys):
    console.disable_logging()
    console.clear_logs()
    captured = capsys.readouterr()
    print(captured.out)
    assert "Logging is not enabled. No logs to clear." in captured.out

def test_clear_logs(capsys):
    console.enable_logging('test_logs.log', 'DEBUG')
    console.debug("Debug message", verbose=True)
    console.info("Info message", verbose=True)
    console.clear_logs()
    logs = console.view_logs()
    assert logs == ""
    console.clear_logs()

def test_save_logs_no_logging_enabled(capsys):
    console.disable_logging()
    console.save_logs('saved_logs.log')
    captured = capsys.readouterr()
    print(captured.out)
    assert "Logging is not enabled. No logs to clear." in captured.out

def test_save_logs(capsys):
    console.enable_logging('test_logs.log', 'DEBUG')
    console.debug("Debug message", verbose=True)
    console.info("Info message", verbose=True)
    console.save_logs('saved_logs.log')
    assert os.path.exists('saved_logs.log')
    console.clear_logs()

# Cleanup
def teardown_module(module):
    try:
        console.disable_logging()  # Disable logging to release the log file
        os.remove('test_logs.log')
        os.remove('saved_logs.log')
    except FileNotFoundError:
        pass