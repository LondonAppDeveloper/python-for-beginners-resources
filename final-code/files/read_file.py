file_path = 'message.txt'

with open(file_path) as msg_file:
    msg = msg_file.read()


print(msg)