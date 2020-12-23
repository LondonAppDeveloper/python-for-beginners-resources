import os

with open('alphabet.txt', 'rb') as af:
    print('Every other letter:')
    while True:
        letter = af.read(1)
        if letter:
            print(letter.decode())
            af.seek(1, os.SEEK_CUR)
        else:
            break
    print('Last letter:')
    af.seek(-1, os.SEEK_END)
    print(af.read(1).decode())