
def unique_elements(*args):
    result = []
    for arg in args:
        if arg not in result:
            result.append(arg)
    return result

print(unique_elements(1, 2, 3, 2, 4, 3, 5))


def my_function(arg1, arg2, arg3=None, arg4=None, arg5=None):
    result = arg1 + arg2
    if arg3 is not None:
        result *= arg3
    if arg4 is not None:
        result -= arg4
    if arg5 is not None:
        result += arg5
    return result
result1 = my_function(1, 2)
result2 = my_function(1, 2, 3)
result3 = my_function(1, 2, arg4=4, arg5=5)




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






