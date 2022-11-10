# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
# [4, 2, 4, 9]
#
# out
# 8
from random import randint


def Create(n):
    list = []
    for i in range(n):
        list.append(randint(-10, 10))
    return list


def Sum_NonDouble(list):
    sum = 0
    for i in range(0, len(list), 2):
        sum += list[i]
    return sum


list = Create(int(input("Введите число элементов массива: ")))
print(list)
print(Sum_NonDouble(list))
