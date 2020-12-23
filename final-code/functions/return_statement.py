def create_greeting(name, age, location):
    """Create and return a greeting with a users name, age and location."""
    message = f'Welcome {name} who is {age} and from {location}.'

    return message


greeting = create_greeting('Mark', 31, 'London')
print(f'Greeting: {greeting}')