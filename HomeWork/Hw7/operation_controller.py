from operations.math_degree import degree
from operations.math_multy import multyply
from operations.math_remainder import reminder
from operations.math_div import devision
from operations.math_sub import subversion
from operations.math_summ import addition
from operations.math_integer_division import integer_devision


def operation(a, b, operation_id):
    if operation_id == 1:
        return addition(a, b)
    elif operation_id == 2:
        return subversion(a, b)
    elif operation_id == 3:
        return multyply(a, b)
    elif operation_id == 4:
        return devision(a, b)
    elif operation_id == 5:
        return degree(a, b)
    elif operation_id == 6:
        return integer_devision(a, b)
    elif operation_id == 7:
        return reminder(a, b)
    else:
        print("Непредвиденная ошибка в блоке operations\n")
