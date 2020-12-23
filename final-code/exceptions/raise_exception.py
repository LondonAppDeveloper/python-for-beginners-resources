def add_name(name):
    """Add a new name to the database."""
    if len(name) < 2:
        raise ValueError('Name is too short.')
    print(f'Name added: {name}')


try:
    add_name('aaaa')
except ValueError as ve:
    print(f'Unable to add name: {str(ve)}')