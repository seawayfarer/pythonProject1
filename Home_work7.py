import random
from functools import wraps

def retry(attempts=5, desired_value=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                result = func(*args, **kwargs)
                if result == desired_value:
                    return result
            print(f"Could not get the desired value {desired_value} after {attempts} attempts.")
        return wrapper
    return decorator


@retry(desired_value=3)
def get_random_value_with_default_attempts():
    return random.choice((1, 2, 3, 4, 5))


@retry(desired_value=[1, 2])
def get_random_values_with_default_attempts(choices, size=2):
    return random.choices(choices, k=size)


@retry(attempts=7, desired_value=3)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(attempts=2, desired_value=[1, 2, 3])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)

print(get_random_value())
print(get_random_value_with_default_attempts())
print(get_random_values_with_default_attempts([1, 2, 3, 4]))
print(get_random_values_with_default_attempts([1, 2, 3, 4], 2))
print(get_random_values_with_default_attempts([1, 2, 3, 4], size=2))
print(get_random_values_with_default_attempts(choices=[1, 2, 3, 4], size=2))
print(get_random_values([1, 2, 3, 4]))
print(get_random_values([1, 2, 3, 4], 3))
print(get_random_values([1, 2, 3, 4], size=1))


def copy_file(src_file_path, dest_file_path):
    with open(src_file_path, 'r') as src_file:
        with open(dest_file_path, 'w') as dest_file:
            dest_file.write(src_file.read())

# example
copy_file('path/to/source/file.txt', 'path/to/destination/file.txt')


import os

def analyze_file(file_path):
    lines_count = 0
    file_size = os.path.getsize(file_path)
    char_counts = {}

    with open(file_path, 'r') as f:
        for line in f:
            lines_count += 1
            line = line.strip()
            for char in line:
                if char != ' ':
                    char_counts[char] = char_counts.get(char, 0) + 1

    top_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    top_chars = [char[0] for char in top_chars]

    return {'lines_count': lines_count, 'file_size': file_size, 'top_chars': top_chars}

result = analyze_file('big.txt')

print(result) # {'lines_count': 128457, 'file_size': 6488666, 'top_chars': ['e', 't', 'a']}
