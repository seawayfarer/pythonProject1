import random
import string
import time

PASSWORD_LENGTH = 4
PASSWORD = 'AbCd'


def generate_password():
    chars = string.ascii_letters  # Генерує всі літери латинського алфавіту
    return ''.join(random.choice(chars) for _ in range(PASSWORD_LENGTH))


def password_checker(password):
    for real_pass_char, passed_pass_char in zip(PASSWORD, password):
        if real_pass_char != passed_pass_char:
            return False
        time.sleep(0.1)
    return True


