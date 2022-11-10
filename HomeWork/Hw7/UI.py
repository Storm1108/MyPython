from exception import float_ex
from operation_controller import operation


def UI_launch():
    a, b, n = 0, 0, 0
    while float_ex(a, b, n):
        a = input('1')
        b = input('2')
        n = input('op')
        print(operation(a, b, n))


UI_launch()
