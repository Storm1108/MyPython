import math_degree, math_multy, math_remainder, math_div, math_sub, math_summ, math_integer_division


def operation(a, b, operation_id):
    if operation_id == 1:
        return math_summ.addition(a, b)
    elif operation_id == 2:
        return math_sub.subversion(a, b)
    elif operation_id == 3:
        return math_multy.multyply(a, b)
    elif operation_id == 4:
        return math_div.devision(a, b)
    elif operation_id == 5:
        return math_degree.degree(a, b)
    elif operation_id == 6:
        return math_integer_division.integer_devision(a, b)
    elif operation_id == 7:
        return math_remainder.reminder(a, b)
    else:
        print("Непредвиденная ошибка в блоке operations\n")
