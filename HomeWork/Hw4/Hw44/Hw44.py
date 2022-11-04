# 4.* Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 1 - 2 = 0
from random import randint


def create(n):
    list = []
    for i in range(n):
        list.append(randint(-10, 10))
    return list


def output(numbers):
    string = str(numbers[0]) + "*x^" + str(len(numbers) - 1)
    i = 1
    while i < len(numbers) - 1:
        if numbers[i] > 0:
            string += " +" + str(numbers[i]) + "*x^" + str(len(numbers) - i - 1)
        elif numbers[i] < 0:
            string += " " + str(numbers[i]) + "*x^" + str(len(numbers) - i - 1)
        i += 1
    if numbers[-1] > 0:
        string += " +" + str(numbers[-1]) + " = 0"
    elif numbers[-1] < 0:
        string += " " + str(numbers[-1]) + " = 0"

    with open('File.txt', 'a') as data:
        data.write(string + "\n")


def main():
    output(create(int(input("Введите степень 1 многочлена: "))))
    output(create(int(input("Введите степень 2 многочлена: "))))
    output(create(int(input("Введите степень 3 многочлена: "))))
    with open('File.txt', 'a') as data:
        data.write("\n")


main()
