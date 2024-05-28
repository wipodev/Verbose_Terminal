# Verbose Terminal [![Python](https://img.shields.io/pypi/v/verbose-terminal.svg)](https://pypi.org/project/verbose-terminal/) [![Downloads](https://static.pepy.tech/badge/verbose-terminal)](https://pepy.tech/project/verbose-terminal)

## Description

Verbose Terminal is a Python library that provides a simple and easy-to-use interface for displaying styled messages in the terminal. It includes predefined styles for success, warning, error, and informational messages, both with and without background colors.

## Requirements

- Python 3.10+

## Installation

You can install the package via pip:

```bash
pip install verbose-terminal
```

## Usage

Import the `Msg` class from the `verbose_terminal` module and use its methods to print styled messages. The following examples demonstrate how to use the library:

### Basic Usage

```python
from verbose_terminal import Msg

# Displaying messages with different styles
Msg.success("Operation completed successfully!", verbose=True)
Msg.warning("This is a warning message.", verbose=True)
Msg.error("An error has occurred.", verbose=True)
Msg.info("Here is some information.", verbose=True)
```

### Light Styles (Text Only)

```python
from verbose_terminal import Msg

# Displaying messages with text styles only
Msg.success_light("Success message without background", verbose=True)
Msg.warning_light("Warning message without background", verbose=True)
Msg.error_light("Error message without background", verbose=True)
Msg.info_light("Info message without background", verbose=True)
```

## Verbose Flag

By default, the `verbose` flag is set to `False`. This means that the messages will not be displayed in the terminal. To display the messages in the terminal, set the `verbose` flag to `True`.

```python
from verbose_terminal import Msg

# Displaying messages in the terminal
Msg.success("This message will be displayed.", verbose=True)
Msg.success("This message will not be displayed.", verbose=False)
```

## Using `msg` Method Directly

```python
from verbose_terminal import Msg

# Displaying messages in the terminal
Msg.msg("This is a plain message", verbose=True)
Msg.msg("This message will not be displayed", verbose=False)
```

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push your branch to GitHub.
4. Submit a pull request.

Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details.

## Running Tests

To run the tests, run the following command:

```bash
pytest -s
```

This will execute the unit tests and display the styled messages in the terminal, allowing you to visually verify the output.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/wipodev/Verbose_Terminal/blob/main/LICENSE) file for more details.

---

Feel free to explore the code and customize the styles as per your requirements. If you encounter any issues or have suggestions for improvements, please open an issue on GitHub.
