lst = [1, 2, [3, 4, [5, 6], 7], 8]


def recursive_sum(lst):
    total_sum = 0
    for elem in lst:
        if type(elem) == int:
            total_sum += elem
        elif type(elem) == list:
            total_sum += recursive_sum(elem)
    return total_sum


print(recursive_sum(lst))


def repeat_words(words, num):
    count = num // len(words) + 1
    repeated_words = [word for word in words for i in range(count)]
    return repeated_words[:num]


words = ["hello", "world"]
num = 5
repeated_words = repeat_words(words, num)
print(repeated_words)


import random
import string
import time

PASSWORD_LENGTH = 4
PASSWORD = 'AbCd'


def generate_password():
    chars = string.ascii_letters
    return ''.join(random.choice(chars) for _ in range(PASSWORD_LENGTH))


def password_checker(password):
    for real_pass_char, passed_pass_char in zip(PASSWORD, password):
        if real_pass_char != passed_pass_char:
            return False
        time.sleep(0.1)
    return True
