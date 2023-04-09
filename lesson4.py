a = 4
b = 3
def printMax():
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


x = 23.1
f = 23.2
d = 22.9

def printMin():
    if f > x > d:
        print(d, 'is minimum')
    elif f > x <= d:
        print(f, 'is maximum')
    else:
        print(x, 'is minimum')


y = 28

def example(y):
    return max(-y, y)


def my_func1(g, h):
    return g + h


print(my_func1(8, 12))


n = 0.001


def my_func2(n):
    if n > 0:
        print('positive')
    elif n < 0:
        print('negative')


print(my_func2(n))











