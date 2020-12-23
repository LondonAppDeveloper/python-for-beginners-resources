import json


with open('output/user.json') as jf:
    user = json.load(jf)

print(type(user))
print(user)

fav_nums = user['fav_nums']
print(type(fav_nums))
print(fav_nums)