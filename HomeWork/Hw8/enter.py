def int_define(text, is_between, minim, maxim):
    number = input(text)
    try:
        number = int(number)
        if (minim <= number <= maxim) and is_between:
            return number
        elif not (minim <= number <= maxim) and is_between:
            print(f"Введите число от {minim} до {maxim}")
            return False
        else:
            return number
    except ValueError:
        print("Введите корректное числовое значение")
        return False
    # except Exception:
    #     print("Непредвиденная ошибка в int_define")


def float_define(text, is_between, minim, maxim):
    number = input(text)
    try:
        number = float(number)
        if (minim <= number <= maxim) and is_between:
            return number
        elif not (minim <= number <= maxim) and is_between:
            print(f"Введите число от {minim} до {maxim}")
            return False
        else:
            return number
    except ValueError:
        print("Введите корректное числовое значение")
        return False
    except Exception:
        print("Непредвиденная ошибка в float_define")


def enter(function, text, is_between=False, minim=0, maxim=0):
    number = function(text, is_between, minim, maxim)
    while type(number) == bool:  # Не использовал not number для ловли 0
        number = function(text, is_between, minim, maxim)
    return number


def date_enter(text):
    print(text)
    year = enter(int_define, 'Введите год: ', True, 0, 2022)
    month = enter(int_define, 'Введите месяц: ', True, 0, 12)
    day = enter(int_define, 'Введите число: ', True, 0, 31)
    if month < 10:
        month = "0" + str(month)
    if day < 10:
        day = "0" + str(day)
    return f'{year}-{month}-{day}'


def time_enter(text):
    print(text)
    hour = enter(int_define, 'Введите час в 24ч формате: ', True, 0, 24)
    minute = enter(int_define, 'Введите минуты: ', True, 0, 60)
    if hour < 10:
        hour = "0" + str(hour)
    if minute < 10:
        minute = "0" + str(minute)
    return f'{hour}:{minute}'


# # print(enter(int_define, 'Введите число: '))
# # print(enter(int_define, 'Введите число: ', True, 0, 12))
# print(date_enter('Введите дату устройства на работу'))
