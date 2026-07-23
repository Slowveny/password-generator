import random, string
from checker import check_password

def password_generator(length, settings, required):
    while True:
        generated_password = ""
        random_digits = ""

        if settings["digits"]:
            random_digits += string.digits

        if settings["symbols"]:
            random_digits += string.punctuation
        
        if settings["uppercase"]:
            random_digits += string.ascii_uppercase
                                
        if settings["lowercase"]:
            random_digits += string.ascii_lowercase
        
        if not required:
            return "Error: no characteres"
    
        while len(generated_password) < length:
            generated_password += random.choice(random_digits)

        if check_password(generated_password, settings):
            return generated_password