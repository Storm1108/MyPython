from complex import _complex_


def complex_ex(a, b, operation_id):
    if type(a) == complex and type(b) == complex and str(operation_id).isdigit() and (1 <= float(operation_id) <= 5):
        return True
    elif type(a) != complex or type(b) != complex:
        print("Ошибка в действии с комплексным числом: входные данные не комплексные")
        return False
    elif not str(operation_id).isdigit():
        print("Введен неверный ключ операции")
        return False
    elif not (1 <= float(operation_id) <= 5):
        print("Данная операция не выполнима с комплексными числами")
        return False
    else:
        print("Непредвиденная ошибка в блоке exception")
        return False


def complex_enter(a1, a2):
    try:
        float(a1)
        float(a2)
        return _complex_(a1, a2)
    except TypeError:
        print("Неверные входные данные: код 0")
        return False
    except ValueError:
        print("Неверные входные данные: код 1")
        return False
    except Exception:
        print("Непредвиденная  ошибка в блоке exception")
        return False


def float_ex(a, b, operation_id=0):
    try:
        if type(a) == float and type(b) == float and str(operation_id).isdigit() and (1 <= float(operation_id) <= 7):
            operation_id = int(operation_id)
            return True
        elif not (type(a) == float and type(b) == float):
            print("Ошибка в действии с рациональным числом: входные данные не рациональные")
            return False
        elif not (str(operation_id).isdigit() and (1 <= float(operation_id) <= 7)):
            print("Введен неверный ключ операции: код 0")
            return False
        else:
            print("Непредвиденная ошибка в блоке exception:try")
            return False
    except TypeError:
        print("Введен неверный ключ операции: код 1")
        return False
    except ValueError:
        print("Неверные входные данные: код 2")
        return False
    except Exception:
        print("Непредвиденная ошибка в блоке exception:except")
        return False


def float_enter(number):
    try:
        return float(number)
    except TypeError:
        print("Неверные входные данные: код 0")
        return False
    except ValueError:
        print("Неверные входные данные: код 1")
        return False
    except Exception:
        print("Непредвиденная  ошибка в блоке exception")
        return False


def UI_ex(char, limit):
    try:
        char = int(char)
        if type(char) == int and (1 <= char <= limit):
            return char
        else:
            return False
    except TypeError:
        print("Неверные входные данные: код 0")
        return False
    except ValueError:
        print("Неверные входные данные: код 1")
        return False
    except Exception:
        print("Непредвиденная  ошибка в блоке exception")
        return False


def main_exception(function):
    try:
        function

    except Exception:
        print(f"Непредвиденная ошибка проекта: {Exception}")
