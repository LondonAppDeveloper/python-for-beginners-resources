fruit = ['Apple', 'Orange', 'Pear', 'Apple', 'Orange', 'Lemon']

print(fruit)

# Convert to set
fruit_set = set(fruit)
print(f'Fruit as set: {fruit_set}')

# Convert back to list
unique_fruit_list = list(fruit_set)
print(f'Unique fruit list: {unique_fruit_list}')

# Make list unique (short)
unique_list = list(set(fruit))
print(f'Unique fruit list: {unique_list}')