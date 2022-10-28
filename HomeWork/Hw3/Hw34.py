# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
from random import random


def Create(n):
    list = []
    for i in range(n):
        list.append(round(random() * 20 - 10, 3))
    return list


def LeftOverDefine(a):
    if a > 0:
        return round(a % 1, 3)
    else:
        return round(1 - a % 1, 3)


def Logic(array):
    print(array)
    leftOvers = list(map(LeftOverDefine, array))
    leftOvers.sort()
    return (leftOvers[0], leftOvers[-1], round(leftOvers[-1] - leftOvers[0], 3))


numbers = Create(10)
i, j, k = Logic(numbers)
print("Min {0}, Max {1} ---> Difference {2}".format(i, j, k))
