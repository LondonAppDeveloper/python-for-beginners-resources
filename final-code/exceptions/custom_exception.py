class ValidationError(Exception):
    """Exception raised for validation errors."""
    
    def __init__(self, field, msg):
        """Set error details."""
        self.field = field
        self.msg = msg


def register(username, password):
    """Register a new user in the system."""
    if not username:
        raise ValidationError('username', 'Field is required.')
    if not password:
        raise ValidationError('password', 'Field is required.')
    print('Registered new user.')


try:
    register('aaa', '')
except ValidationError as ve:
    print(f'Error validating {ve.field}: {ve.msg}')


