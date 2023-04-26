
def unique_elements(*args):
    result = []
    for arg in args:
        if arg not in result:
            result.append(arg)
    return result

print(unique_elements(1, 2, 3, 2, 4, 3, 5))


def my_function(arg1, arg2, /, arg3=None, *, arg4=None, arg5='default_value_1', arg6='default_value_2'):
    pass


def outer_func(num):
    def inner_func(num2):
        return num * num2
    return inner_func
func = outer_func(5)
result = func(10)
print(result)


def print_square(size, end_marker=None):
    if size <= 0:
        if end_marker is not None:
            print(end_marker)
        return

    print('*' * size)
    print_square(size - 1, end_marker)

print_square(5, '---')






