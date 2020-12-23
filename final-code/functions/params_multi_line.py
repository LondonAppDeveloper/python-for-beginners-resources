def output_welcome_text(first_name, 
                        last_name, 
                        age, 
                        location, 
                        returning_user=True):
    """Output welcome text with users details"""
    if returning_user:
        msg_start = f'Welcome back {first_name} {last_name}!'
    else:
        msg_start = f'Welcome {first_name} {last_name}!'
    msg = f'{msg_start} You are {age} and from {location}.'
    print(msg)


output_welcome_text(
    'Mark', 
    'W', 
    age=31, 
    location='London',
)
