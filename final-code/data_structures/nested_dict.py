dog = {
    'name': 'Otis',
    'breed': 'Pug',
    'owner': {
        'name': 'Mark',
        'age': 31,
    }
}
print(dog)

owner_name = dog['owner']['name']
print(f'Owner Name: {owner_name}')