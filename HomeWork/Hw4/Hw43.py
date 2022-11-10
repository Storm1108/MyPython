# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]
from random import randint


def Create(n):
    list = []
    for i in range(n):
        list.append(randint(0, 10))
    return list


def Exclude(array):
    temp = []
    for i in array:
        if (i not in temp) and (array.count(i) > 1):
            temp.append(i)
    return [k for k in array if k not in temp]


array = Create(10)
print(array)
print(Exclude(array))
