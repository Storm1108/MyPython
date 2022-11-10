def complex_ex(a, b, operation_id=0):
    if type(a) == complex and type(b) == complex and (0 <= operation_id <= 5) and type(operation_id) == int:
        return True
    elif type(a) != complex or type(b) != complex:
        print("Ошибка в действии с комплексным числом: входные данные не комплексные")
        return False
    elif not (0 <= operation_id <= 5):
        print("Данная операция не выполнима с комплексными числами")
        return False
    elif not type(operation_id) == int:
        print("Введен неверный ключ операции")
        return False
    else:
        print("Непредвиденная ошибка в блоке exception")
        return False


def float_ex(a, b, operation_id=0):
    if str(a).isdigit() and str(b).isdigit() and type(operation_id) == int and (0 <= operation_id <= 7):
        return True
    elif not (str(a).isdigit() and str(b).isdigit()):
        print("Ошибка в действии с рациональным числом: входные данные не рациональные")
        return False
    elif (not type(operation_id) == int) or (0 <= operation_id <= 7):
        print("Введен неверный ключ операции")
        return False
    else:
        print("Непредвиденная ошибка в блоке exception")
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
