def username_func(username):
    name_error = ''

    if len(username) < 3 or len(username) > 20 :
        name_error = "You did not enter a valid username (must be 3-20 characters)"
        
    for let in username:
        if let == ' ':
            name_error = "You did not enter a valid username (may not contain spaces)"

    return name_error

def password_func(password):
    pass_error = ''

    if len(password) < 3 or len(password) > 20 :
            pass_error = "You did not enter a valid password (must be 3-20 characters)"
        
    for char in password:
        if char == ' ':
            pass_error = "You did not enter a valid password (may not contain spaces)"

    return pass_error

def ver_pass_func(password, ver_password):
    ver_pass_error = ''

    if ver_password != password or len(ver_password) == 0:
        ver_pass_error = "Your passwords do not match"
    
    return ver_pass_error

def email_func(email):
    email_error = ''
    address = ''

    if len(email) < 3 or len(email) > 20:
        email_error = "Please enter a valid email"
        return email_error

    for let in email:
        if let == '':
            break
        if let == ' ':
            email_error = "Please enter a valid email"
            break
        if let == "@" or let == ".":
            address+=let

    if len(address) != 2:
        email_error = "Please enter a valid email"

    return email_error