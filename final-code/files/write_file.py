file_path = 'output.txt'

text_lines = [
    'Hello\n',
    'My name is: \n',
    'Mark',
]
with open(file_path, 'a') as out_file:
    out_file.writelines(text_lines)

