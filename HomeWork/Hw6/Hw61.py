# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
from random import randint


def create(n):
    list = []
    for i in range(n):
        list.append(randint(0, 10))
    print(list)
    return list


def main(number):
    array = create(number)
    array_sorted = [array[i] for i in range(1, len(array)) if array[i] > array[i - 1]]
    return array_sorted


print(main(int(input("Введите число элементов: "))))
