def generate_welcome_message(name):
    empty_space1 = ''
    usersnametobeputinmessage = name
    empty_space1 = empty_space1 + ' '
    start_of_message_that_says_welcome_back_with_comma = 'Welcome back,'
    fullstopbecause_punctuationisimportant = '.'
    final_message_readytogo = start_of_message_that_says_welcome_back_with_comma + empty_space1
    final_message_readytogo = final_message_readytogo + usersnametobeputinmessage
    final_message_readytogo = final_message_readytogo + fullstopbecause_punctuationisimportant

    return final_message_readytogo


print(
    generate_welcome_message('Mark')
)
