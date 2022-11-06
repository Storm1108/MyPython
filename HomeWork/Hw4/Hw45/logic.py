# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
# in
# "poly.txt"
# "poly_2.txt"
# out
# The contents of the files do not match!


def summ(list_1, list_2):
    result = []
    min_len = min(len(list_1), len(list_2))
    for i in range(min_len):
        result.append(list_1[i] + list_2[i])
    if len(list_1) > len(list_2):
        for j in range(min_len, len(list_1)):
            result.append((list_1[j]))
    elif len(list_2) > len(list_1):
        for j in range(min_len, len(list_2)):
            result.append((list_2[j]))
    return result


def filtrate(string):
    if string.find('x') != -1:
        return (int(string[:string.find('*')]), int(string[string.find('^') + 1:]))
    else:
        return (int(string), 0)


def read(string):
    # string = str(datafile.readline())
    mass = string.split()
    mass.pop()
    mass.pop()
    mass_copy = []
    if "-" in mass or "+" in mass:
        if not (mass[0] == "+" or mass[0] == "-"):
            mass.insert(0, "+")
        for i in range(0, len(mass), 2):
            mass_copy.append(str(mass[i] + mass[i + 1]))
        mass = mass_copy
    result_temp = []
    for j in mass:
        result_temp.append(filtrate(j))
        result_temp.sort(key=lambda a: a[1], reverse=True)
    length = list(range(max(result_temp, key=lambda a: a[1])[1] + 1))
    result = []
    for k in length:
        sum_k = 0
        for element in result_temp:
            if element[1] == k:
                sum_k += element[0]
        result.append(sum_k)

    while result[-1] == 0:
        result.pop()
    return result


def write(array, file):
    file.write("{}*x^{} ".format(array[0], len(array) - 1))
    for i in range(1, len(array) - 1):
        if array[i] > 0:
            file.write("+{}*x^{} ".format(array[i], len(array) - i - 1))
        elif array[i] < 0:
            file.write("{}*x^{} ".format(array[i], len(array) - i - 1))
    if array[-1] < 0:
        file.write("{}".format(array[-1]))
    elif array[-1] > 0:
        file.write("+{}".format(array[-1]))
    file.write(" = 0\n")


def main_func(path_1, path_2):
    poly_1 = open(path_1, 'r')
    poly_2 = open(path_2, 'r')
    poly_array_1 = poly_1.readlines()
    poly_array_2 = poly_2.readlines()
    poly_1.close()
    poly_2.close()
    resulting_poly_1 = multy_summ(poly_array_1, 1)
    resulting_poly_2 = multy_summ(poly_array_2, 2)
    return summ(resulting_poly_1, resulting_poly_2)


def multy_summ(poly_array,file_num):
    resulting_poly_1 = read(poly_array[0])
    print(f"Индексы 1 приведенного многочлена из 1 строки "
          f"по убыванию степени начиная с наибольшей:  {resulting_poly_1}")
    for line_number_1 in range(1, len(poly_array)):
        poly_current = read(poly_array[line_number_1])
        poly_temp = resulting_poly_1
        poly_current.reverse()
        print( f"Индексы {line_number_1 + 1} приведенного многочлена из {file_num} строки  "
            f"по убыванию степени начиная с наибольшей:  {poly_current}")
        poly_current.reverse()
        resulting_poly_1 = summ(poly_temp, poly_current)
    print(f"Индексы результирующего многочлена {file_num} строки по убыванию степени начиная с наибольшей: {resulting_poly_1}")
    return resulting_poly_1


def main(path_1='files/poly.txt', path_2='files/poly_2.txt'):
    result = main_func(path_1,path_2)
    print(f"\n -------------------------------------------------------------------------------------------\n"
          f"Индексы результирующего многочлена строки по убыванию степени начиная с наибольшей: {result}")
    with (open('Result.txt', 'a')) as final_file:
        write(result, final_file)

def UI_launch():
    try:

        print("Выполнение...")
        check = int(input("Программа читает многочлен из верхней строки каждого файла\n"
                          "Желаете ввести путь к файлам вручную?\n"
                          "1 - Нет\n"
                          "2 - Да\n"
                          "Другой символ - выход\n"))
        if check == 1:
            main()
        elif check == 2:
            main(str(input("Введите путь 1 файла с многочленами: ")),
                      str(input("Введите путь 2 файла с многочленами: ")))
        print("Готово")
    except ValueError:
        print("Error: Ошибка в записи многочлена")
    except IndexError:
        print("Error: Введена текстовая или пустая строка")
    except FileNotFoundError:
        print("Error: Путь к файлу указан неверно")
    except Exception:
        print("Другая ошибка")
    finally:
        print("-------------------------------------")


UI_launch()
