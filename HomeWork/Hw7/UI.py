from exception import float_ex, complex_ent, complex_ex
from operation_controller import operation
from complex import _complex_


def float_enter():
    a = input('Введите 1 число: ')
    b = input('Введите 2 число: ')
    n = input('1 - Сложение a + b\n'
              '2 - Вычитание a - b\n'
              '3 - Умножение a * b\n'
              '4 - Деление a / b\n'
              '5 - Возведение в степень a ^ b\n'
              '6 - Деление без остатка a // b\n'
              '7 - Остаток от деления a % b\n'
              'Введите номер операции: ')
    while not float_ex(a, b, n):
        print("Введите корректные значения: \n")
        a = input('Введите 1 число: ')
        b = input('Введите 2 число: ')
        n = input('1 - Сложение a + b\n'
                  '2 - Вычитание a - b\n'
                  '3 - Умножение a * b\n'
                  '4 - Деление a / b\n'
                  '5 - Возведение в степень a ^ b\n'
                  '6 - Деление без остатка a // b\n'
                  '7 - Остаток от деления a % b\n'
                  'Введите номер операции: ')
    a, b, n = float(a), float(b), int(n)
    return operation(a, b, n)


def complex_enter():
    a = input('Введите целую часть 1 числа: ')
    b = input('Введите мнимую часть 1 числа: ')
    while complex_ent(a, b) == False:
        print("Введите корректные значения: \n")
        a = input('Введите целую часть 1 числа: ')
        b = input('Введите мнимую часть 1 числа: ')
    compl_number_1 = complex_ent(a, b)
    print(compl_number_1)
    a = input('Введите целую часть 2 числа: ')
    b = input('Введите мнимую часть 2 числа: ')
    while complex_ent(a, b) == False:
        print("Введите корректные значения: \n")
        a = input('Введите целую часть 2 числа: ')
        b = input('Введите мнимую часть 2 числа: ')
    compl_number_2 = complex_ent(a, b)
    print(compl_number_2)
    n = input('1 - Сложение a + b\n'
              '2 - Вычитание a - b\n'
              '3 - Умножение a * b\n'
              '4 - Деление a / b\n'
              '5 - Возведение в степень a ^ b\n'
              'Введите номер операции: ')
    while not complex_ex(compl_number_1, compl_number_2, n):
        print("Введите корректное значения: \n")
        n = input('1 - Сложение a + b\n'
                  '2 - Вычитание a - b\n'
                  '3 - Умножение a * b\n'
                  '4 - Деление a / b\n'
                  '5 - Возведение в степень a ^ b\n'
                  'Введите номер операции: ')
    n = int(n)
    return operation(compl_number_1, compl_number_2, n)


def UI_launch():
    float_enter()
    complex_enter()

print(complex_enter())
# UI_launch()
