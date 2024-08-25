# Password Generator

A simple and customizable password generator for Python.

## Features

- Generate passwords of any length.
- Include or exclude uppercase letters, lowercase letters, digits, and special characters.
- Ensure at least one character from each selected category is included.
- Custom error handling for invalid inputs.

## Installation

You can install the package using pip:

```sh
pip install password_generator
```

## Usage
Here’s how to use the password generator in your Python code:
```
from password_generator import generate_password, PasswordGeneratorError

try:
    # Generate a 16-character password with all character types
    print(generate_password(16))

    # Generate a 12-character password with only letters and digits
    print(generate_password(12, use_special=False))

    # Generate an 8-character password with only lowercase letters
    print(generate_password(8, use_uppercase=False, use_digits=False, use_special=False))

    # Example of triggering an error
    print(generate_password(-5))  # This will raise an error

except PasswordGeneratorError as e:
    print(f"Error: {e}")
```


## Parameters
length (int): Length of the password (default is 12). Must be a positive integer.
use_uppercase (bool): Include uppercase letters (default is True).
use_lowercase (bool): Include lowercase letters (default is True).
use_digits (bool): Include digits (default is True).
use_special (bool): Include special characters (default is True).


## Error Handling
Error Handling
The generate_password function raises a PasswordGeneratorError for invalid inputs. Make sure to handle this exception in your code

```from password_generator import generate_password

# Generate a 16-character password with all character types
print(generate_password(16))

# Generate a 12-character password with only letters and digits
print(generate_password(12, use_special=False))

# Generate an 8-character password with only lowercase letters
print(generate_password(8, use_uppercase=False, use_digits=False, use_special=False))
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## Autho
    Vijesh Ghandare - mail.vijeshg@gmail.com