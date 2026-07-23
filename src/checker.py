import string


def check_password(password, settings):
    password = set(password)
    uppercase = set(string.ascii_uppercase)
    lowercase = set(string.ascii_lowercase)
    symbols = set(string.punctuation)
    digits = set(string.digits)




    if settings["uppercase"] and not password.intersection(uppercase):
        return False

    if settings["lowercase"] and not password.intersection(lowercase):
        return False

    if settings["symbols"] and not password.intersection(symbols):
        return False
    
    if settings["digits"] and not password.intersection(digits):
        return False
    
    return True