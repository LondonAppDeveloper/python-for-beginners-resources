with open('alphabet.txt') as af:
    print(f'Location when opening: {af.tell()}')
    print(f'First letter: {af.read(1)}')
    print(f'Second letter: {af.read(1)}')
    af.seek(4)
    print(f'5th letter: {af.read(1)}')