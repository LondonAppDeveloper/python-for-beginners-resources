# Write your code in this file! Good luck.
from exchange import (
    symbol,
    convert,
)


def local_price(amount, currency):
    """Display amount in specified currency."""
    amt = convert(amount, currency)
    sym = symbol(currency)
    return f'{sym}{amt}'
