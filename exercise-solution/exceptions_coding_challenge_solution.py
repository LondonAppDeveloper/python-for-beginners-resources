# Modify this file. Good luck!

class SignUpError(Exception):
    """Error raised when there are issues with sign up."""

    def __init__(self, username, password):
        """Set the username and password in exception."""
        self.username = username
        self.password = password


def sign_up(username, password):
    """Create a new user in the system."""
    # Write your code here

    if len(password) < 5:
        raise SignUpError(username, password)

    print(f'New user created: {username}')
