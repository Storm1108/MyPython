# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import randint
def Create(n):
    list = []
    for i in range(n):
        list.append(randint(-10, 10))
    return list
def Main_Logic(list):
    pairs = []
    for i in range(len(list)//2):
        pairs.append((list[i], list[-(i+1)]))
        print(f"{pairs[i]} ----> {list[i] * list[-(i+1)]}")
    return pairs

list = Create(int(input("Введите число элементов массива: ")))
print(list)
print(Main_Logic(list))