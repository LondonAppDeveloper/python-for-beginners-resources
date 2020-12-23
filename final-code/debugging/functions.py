def add(x, y):
    """Add two numbers together and return result."""
    result = x + y
    
    return result


output_prefix = 'Total:'
total = add(7, 3)
message = f'{output_prefix} {total}'

print(message)