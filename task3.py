import random
import string

def password_generator(length, use_digits=True, use_symbols=True):
    characters = string.ascii_letters  # A-Z and a-z

    if use_digits:
        characters += string.digits  # 0-9
    if use_symbols:
        characters += string.punctuation  # Special characters like !@#$%*&^

    if not characters:
        print("Error: No character is selected.")
        return ""

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter the desired password length: "))
    include_digits = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        password = password_generator(length, include_digits, include_symbols)
        print(f"\nGenerated Password: {password}")
except ValueError:
    print("Invalid input. Please enter a valid number.")