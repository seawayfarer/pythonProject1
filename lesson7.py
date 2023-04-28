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

def generate_password():
    password = ''.join(random.choices(string.ascii_letters, k=4))
    return password

def password_checker(password):
    real_password = 'LiLu' # Initial password for compare
    start_time = time.time()
    for real_pass_char, passed_pass_char in zip(real_password, password):
        if real_pass_char != passed_pass_char:
            return False
        time.sleep(0.1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 0.4:
        return True
    else:
        return False

password = ''
delay = 0.1
for _ in range(4):
    for symbol in string.ascii_letters:
        start = time.time()
        if password_checker(password + symbol):
            password += symbol
            delay += 0.1
            break
        end = time.time()
        if end - start > delay:
            password += symbol
            delay += 0.1
            break

print(f"Find password: {password}")
