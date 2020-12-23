def output_greeting(name):
    """Output a greeting for given name."""
    message = f'Hello {name}!'

    def output_greeting_to_screen():
        """Output the greeting to the screen."""
        print(message)

    output_greeting_to_screen()


output_greeting('Mark')