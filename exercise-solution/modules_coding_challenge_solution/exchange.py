"""
Module which contains exchange rates to and from the dollar.
"""
# DO NOT MODIFY THIS FILE
RATES = {
    'GBP': {'symbol': '£', 'rate': 0.74},
    'INR': {'symbol': '₹', 'rate': 73.56},
    'EUR': {'symbol': '€', 'rate': 0.83},
}

def convert(amount, currency):
    """Takes an amount amount in USD and converts to currency."""
    return round(amount * RATES[currency]['rate'])


def symbol(currency):
    """Takes a 3 letter currency string and returns a symbol."""
    return RATES[currency]['symbol']
# DO NOT MODIFY THIS FILE
