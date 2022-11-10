from complex import _complex_


def complex_ex(a, b, operation_id=0):
    if type(a) == complex and type(b) == complex and str(operation_id).isdigit() and (0 <= float(operation_id) <= 5):
        return True
    elif type(a) != complex or type(b) != complex:
        print("Ошибка в действии с комплексным числом: входные данные не комплексные")
        return False
    elif not str(operation_id).isdigit():
        print("Введен неверный ключ операции")
        return False
    elif not (0 <= operation_id <= 5):
        print("Данная операция не выполнима с комплексными числами")
        return False
    else:
        print("Непредвиденная ошибка в блоке exception")
        return False


def complex_ent(a1, a2):
    try:
        float(a1)
        float(a2)
        return _complex_(a1, a2)
    except TypeError:
        print("Неверные входные данные: код 0")
        return False
    except ValueError:
        print("Неверные входные данные: код 0")
        return False
    except Exception:
        print("Непредвиденная  ошибка в блоке exception")
        return False


def float_ex(a, b, operation_id=0):
    try:
        if str(a).isdigit() and str(b).isdigit() and str(operation_id).isdigit() and (0 <= float(operation_id) <= 7):
            print('Done')
            operation_id = int(operation_id)
            return True
        elif not (str(a).isdigit() and str(b).isdigit()):
            print("Ошибка в действии с рациональным числом: входные данные не рациональные")
            return False
        elif not (str(operation_id).isdigit() and (0 <= float(operation_id) <= 7)):
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


def UI_ex(char, limit):
    if type(char) == int and (1 <= char <= limit):
        return True
    else:
        return False


def main_exception(function):
    try:
        function()
    except Exception:
        print(f"Непредвиденная ошибка проекта: {Exception}")
