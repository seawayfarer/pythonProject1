
def unique_elements(*args):
    result = []
    for arg in args:
        if arg not in result:
            result.append(arg)
    return result

print(unique_elements(1, 2, 3, 2, 4, 3, 5))


def my_function(**kwargs):
    num_args = len(kwargs)
    user_type = kwargs.get("user_type", "Student")
    print("Number of arguments:", num_args)
    print("Тype of user :", user_type)
my_function(name="Ivan", age=25, user_type="Able")
my_function(name="Ivan", age=25)


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

    if end_marker is None:
        end_marker = size

    if end_marker == 0:
        return

    print('*' * size)
    print_square(size, end_marker - 1)

print_square(5, 3)






