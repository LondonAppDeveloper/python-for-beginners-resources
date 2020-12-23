import os

base_dir = os.getcwd()
sub_dir = 'output'
full_dir_path = os.path.join(base_dir, sub_dir)

os.makedirs(full_dir_path, exist_ok=True)

file_path = os.path.join(full_dir_path, 'message.txt')
with open(file_path, 'a') as msg_file:
    msg_file.write('Hello\n')