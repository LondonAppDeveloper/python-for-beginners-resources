import argparse
import os


def handle_args():
    """Handle arguments for script."""
    parser = argparse.ArgumentParser(
        description='Write a range of numbers to a file.'
    )
    parser.add_argument(
        'path',
        help='Path to store file.'
    )
    parser.add_argument(
        '-s', '--start',
        help='Start of range to print to file.',
        type=int,
        default=1,
    )
    parser.add_argument(
        '-f', '--finish',
        help='Finish of range to print to file.',
        type=int,
        default=100,
    )
    parser.add_argument(
        '-d', '--create-dirs',
        help='Create sub directories for file output.',
        action='store_true'
    )

    return parser.parse_args()


def main():
    """Entrypoint to script."""
    args = handle_args()

    if args.create_dirs:
        dir_path = os.path.dirname(args.path)
        os.makedirs(dir_path, exist_ok=True)

    with open(args.path, 'w') as f:
        for x in range(args.start, args.finish):
            f.write(f'{str(x)}\n')


if __name__ == '__main__':
    main()