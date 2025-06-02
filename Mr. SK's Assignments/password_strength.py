password = input('Enter your password: ')


password_length = len(password)
if password_length < 8: print('Your password is very weak')
if password_length == 8: print('Your password is weak')
if password_length > 8 and password_length < 16: print('Your password is strong')
if password_length > 16: print('Your password is very strong')