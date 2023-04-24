s = "Hello, world!"
s[::-1]

length = len(s)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = "|".join(str(x) for x in my_list[2::3])


def symbol_count_1(s):
    result = {}
    for c in s:
        result[c] = s.count(c)
    return result

print(symbol_count_1('Hello, world!'))


def symbol_count_2(s):

    result = {}
    for c in s:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result

print(symbol_count_2('Hello, world!'))


strings = ["hello", "world", "this is a test"]

def longest_string(strings):
    longest = ""
    for s in strings:
        if len(s) > len(longest):
            longest = s
    return longest


s = "c/a/b"
separator = "/"

def divide_and_glue(s, separator):
    words = s.split(separator)
    words_sorted = sorted(words)
    result = separator.join(words_sorted)
    return result


lst = [119, 101, 108, 108, 32, 100, 111, 110, 101]

def ascii_string(lst):
    result = ""
    for num in lst:
        result += chr(num)
    return result



























