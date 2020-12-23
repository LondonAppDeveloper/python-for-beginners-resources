def output_welcome_text(name, returning_user=True):
    """Output welcome text with provided name."""
    if returning_user:
        message = f'Welcome back {name}!'
    else:
        message = f'Welcome {name}!'
    print(message)


output_welcome_text(name='Mark')
output_welcome_text('Daisy', False)
output_welcome_text('Brooke', returning_user=True)