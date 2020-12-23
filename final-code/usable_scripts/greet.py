import argparse


greetings = {
    'english': 'Hello',
    'french': 'Bonjour',
    'german': 'Hallo',
    'italian': 'Ciao',
}


def handle_args():
    """Parse and return arguments."""
    parser = argparse.ArgumentParser(description='Generate a greeting.')
    parser.add_argument('first_name', help='First name of person to greet.')
    parser.add_argument('last_name', help='Last name of person to greet.')
    parser.add_argument(
        '-l', '--language',
        help='Language of greeting.',
        choices=greetings.keys(),
        default='english',
    )

    return parser.parse_args()


def main():
    """Entrypoint to script."""
    args = handle_args()
    greeting = greetings[args.language]
    print(f'{greeting}, {args.first_name} {args.last_name}.')


if __name__ == '__main__':
    main()