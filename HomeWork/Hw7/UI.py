from exception import float_ex, complex_enter, complex_ex, float_enter, UI_ex
from operation_controller import operation
from logging import _log_
from complex import _complex_


def float_operation():
    a = input('Введите 1 число: ')
    while float_enter(a) == False:
        print("Введите корректные значения: \n")
        a = input('Введите 1 число: ')
    b = input('Введите 2 число: ')
    while float_enter(b) == False:
        print("Введите корректные значения: \n")
        b = input('Введите 2 число: ')
    a, b = float(a), float(b)
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
        n = input('1 - Сложение a + b\n'
                  '2 - Вычитание a - b\n'
                  '3 - Умножение a * b\n'
                  '4 - Деление a / b\n'
                  '5 - Возведение в степень a ^ b\n'
                  '6 - Деление без остатка a // b\n'
                  '7 - Остаток от деления a % b\n'
                  'Введите номер операции: ')
    n = int(n)
    result = operation(a, b, n)
    print(f'{a}{operation_dikt[n]}{b} ---> {result}')
    _log_(operation_dikt[n], a, b, result)
    return result


def complex_operation():
    a = input('Введите целую часть 1 числа: ')
    b = input('Введите мнимую часть 1 числа: ')
    while complex_enter(a, b) == False:
        print("Введите корректные значения: \n")
        a = input('Введите целую часть 1 числа: ')
        b = input('Введите мнимую часть 1 числа: ')
    compl_number_1 = complex_enter(a, b)
    print(compl_number_1)
    a = input('Введите целую часть 2 числа: ')
    b = input('Введите мнимую часть 2 числа: ')
    while complex_enter(a, b) == False:
        print("Введите корректные значения: \n")
        a = input('Введите целую часть 2 числа: ')
        b = input('Введите мнимую часть 2 числа: ')
    compl_number_2 = complex_enter(a, b)
    print(compl_number_2)
    n = input('1 - Сложение a + b\n'
              '2 - Вычитание a - b\n'
              '3 - Умножение a * b\n'
              '4 - Деление a / b\n'
              '5 - Возведение в степень a ^ b\n'
              'Введите номер операции: ')
    while not complex_ex(compl_number_1, compl_number_2, n):
        print("Введите корректное значения: \n")
        n = input('Введите номер операции:\n'
                  '1 - Сложение a + b\n'
                  '2 - Вычитание a - b\n'
                  '3 - Умножение a * b\n'
                  '4 - Деление a / b\n'
                  '5 - Возведение в степень a ^ b\n'
                  'Ваш выбор: ')
    n = int(n)
    result = operation(compl_number_1, compl_number_2, n)
    print(f'{compl_number_1}{operation_dikt[n]}{compl_number_2} ---> {result}')
    _log_(operation_dikt[n], compl_number_1, compl_number_2, result)
    return result

def choice_loop():
    choice = input("Выберете тип чисел для подсчета\n"
                   "1 - Рациональные\n"
                   "2 - Комплексные\n"
                   "3 - Выход из калькуятора\n"
                   "Ваш выбор: ")
    while UI_ex(choice, 3) == False:
        print("Введите корректное значения: \n")
        choice = input("Выберете тип чисел для подсчета\n"
                       "1 - Рациональные\n"
                       "2 - Комплексные\n"
                       "3 - Выход из калькуятора\n"
                       "Ваш выбор: ")
    return int(choice)


def UI_launch():
    choice = 0
    while choice != 3:
        choice = choice_loop()
        if choice == 1:
            float_operation()
        elif choice == 2:
            complex_operation()
        elif choice == 3:
            print("Выход из калькулятора...")


operation_dikt = {1: ' + ', 2: ' - ', 3: ' * ', 4: ' / ', 5: ' ^ ', 6: ' // ', 7: ' % '}

UI_launch()