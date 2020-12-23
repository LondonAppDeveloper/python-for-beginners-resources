import json

user = {
    'name': 'Mike',
    'age': 56,
    'is_active': True,
    'fav_nums': [1, 6, 3, 8, 4],
}

user_str = json.dumps(user)

print(type(user_str))
print(user_str)