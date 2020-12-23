cart = []

try:
    item = cart[1]
except IndexError:
    print('Item with index not found.')