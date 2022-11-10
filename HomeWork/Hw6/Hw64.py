# 4. * Функция принимает в качестве аргументов строки в формате «Имя Фамилия»,
# возвращает словарь, ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Юнона Ветрякова", "Борис Аркадьев", "Антон Серов", "Павел Анисимов"
# out
#
# {'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']},
#  'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']},
#  'И': {'И': ['Илья Иванов']},
#  'В': {'Ю': ['Юнона Ветрякова']}}
def surname_dikt_array(name, names):
    array = [elem for elem in names if elem[elem.find(' ') + 1] == name[name.find(' ') + 1]]
    return sorted(array)


def name_sorted_dict(names):
    dikt = {name[0]: [elem for elem in names if elem[0] == name[0]] for name in names}
    dikt = dict(sorted(dikt.items()))
    return dikt


def _main_(names_str):
    names = [elem.strip().strip('"') for elem in names_str.split(",")]
    dikt_surnames = {name[name.find(' ') + 1]: name_sorted_dict(surname_dikt_array(name, names)) for name in names}
    return dikt_surnames


print(_main_(input()))
