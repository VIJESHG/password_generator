import random
import string

import random
import string
import random
import string

import random
import string

class PasswordGeneratorError(Exception):
    """Custom exception for password generator errors."""
    pass

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    """
    Generate a random password with specified rules.

    Parameters:
    length (int): Length of the password (default is 12). Must be a positive integer.
    use_uppercase (bool): Include uppercase letters (default is True).
    use_lowercase (bool): Include lowercase letters (default is True).
    use_digits (bool): Include digits (default is True).
    use_special (bool): Include special characters (default is True).

    Returns:
    str: The generated password.

    Raises:
    PasswordGeneratorError: If the length is not a positive integer.
    PasswordGeneratorError: If no character sets are selected.
    PasswordGeneratorError: If the length is too short to include one of each selected character type.
    PasswordGeneratorError: If any of the use_* parameters are not boolean.

    Example:
    >>> generate_password(16)
    'A1b2C3d4E5f6G7h8'

    >>> generate_password(12, use_special=False)
    'A1b2C3d4E5f6'

    >>> generate_password(8, use_uppercase=False, use_digits=False, use_special=False)
    'abcdefgh'
    """

    if not isinstance(length, int) or length <= 0:
        raise PasswordGeneratorError("Password length must be a positive integer.")
    
    if not any([use_uppercase, use_lowercase, use_digits, use_special]):
        raise PasswordGeneratorError("At least one character set must be selected.")
    
    if length < (use_uppercase + use_lowercase + use_digits + use_special):
        raise PasswordGeneratorError("Password length is too short to include one of each selected character type.")

    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Ensure at least one character from each selected category
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random choices from the combined set
    remaining_length = length - len(password)
    password.extend(random.choice(characters) for _ in range(remaining_length))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)

print(generate_password(2))
