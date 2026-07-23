from generator import password_generator


def ask_yes_no(message):
    while True:
        answer = input(message).lower()

        if answer in ('y', 'n'):
            return answer == 'y'

        print("Please enter Y or N.")


include_numbers = ask_yes_no("Include numbers? [Y / N]: ")
include_symbols = ask_yes_no("Include symbols? [Y / N]: ")
include_uppercase = ask_yes_no("Include uppercase letters? [Y / N]: ")
include_lowercase = ask_yes_no("Include lowercase letters? [Y / N]: ")

password_settings = {
            "digits": include_numbers,
            "symbols": include_symbols,
            "uppercase": include_uppercase,
            "lowercase": include_lowercase
           }

required = sum(password_settings.values())

while True:
    if required > 0:
        print()
        print(f"WARNING: The password length must be at least {required} characters long.")
        length_password = input("Password length: ")

        if length_password.isdigit() and int(length_password) >= required:
            length_password = int(length_password)
            break
    else:
        length_password = 0
        break

password = password_generator(length_password, password_settings, required)

print()
print("Generated password:")
print(password)