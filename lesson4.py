a = 4
b = 3


def maximum(a, b):
    if a > b:
        return a
    else:
        return b


x = 23.1
f = 23.2
d = 22.9


def minimum(f, x, d):
    if f > x > d:
        return d
    else d < f > x:
        return x


y = 28


def modul(y):
    return max(-y, y)


def addition(g, h):
    return g + h


print(addition(8, 12))


n = 0.001


def value_of_number(n):
    if n > 0:
        print('positive')
    elif n < 0:
        print('negative')
    else:
        print(None)


value_of_number(n)
