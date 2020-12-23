names = ['Brooke', 'Mark', 'Daisy']

# Update name by index
names[2] = 'Diva'

# Append name
names.append('Greg')

# Extend list with 3 more items
names.extend(['Sadie', 'Diva', 'James'])

# Remove name
names.remove('Mark')

# Remove first name from list
removed_from_list = names.pop(0)
print(f'Removed: {removed_from_list}')

# Print list of names
print(names)
# Print name as specific index
print(names[2])

if 'Greg' in names:
    print('Greg is in the list.')

if 'Mark' not in names:
    print('Mark is NOT in the list.')