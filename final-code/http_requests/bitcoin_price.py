"""
Get bitcoin price.
"""
import argparse
import requests


def _price_url(currency, action):
    """Generate coinbase price URL."""
    return f'https://api.coinbase.com/v2/prices/BTC-{currency}/{action}'


def handle_args():
    """Process arguments."""
    parser = argparse.ArgumentParser(description='Get bitcoin price.')
    parser.add_argument(
        '-c', '--currency',
        help='Currency code.',
        choices=['GBP', 'USD', 'INR'],
        default='USD'
    )
    parser.add_argument(
        '-a', '--action',
        help='Action to perform.',
        choices=['buy', 'sell'],
        default='buy'
    )

    return parser.parse_args()


def main():
    """Entrypoint to script."""
    args = handle_args()
    url = _price_url(args.currency, args.action)
    res = requests.get(url)

    data = res.json()
    amt = data['data']['amount']
    print(f'Amount: {amt} ({args.currency})')


if __name__ == '__main__':
    main()

