import random
import string
import time


def generate_password():
    # Generate a random 4-character password consisting of uppercase and lowercase letters
    password = ''.join(random.choices(string.ascii_letters, k=4))
    return password


def password_checker(password):
    # Generate a real password to check against
    real_password = generate_password()

    # Check each character of the guessed password against the real password
    for real_pass_char, passed_pass_char in zip(real_password, password):
        if real_pass_char != passed_pass_char:
            return False
        time.sleep(0.1)
    return True

# Generate a random password and check it
password = generate_password()
print("Guessed password:", password)
if password_checker(password):
    print("Password is correct!")
else:
    print("Password is incorrect.")

