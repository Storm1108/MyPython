# 4. Напишите программу, которая принимает на вход 2 числа.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

a = int(input("Position one: "))
b = int(input("Position two: "))
n = int(input("N: "))
numbers_list = list(range(-n, n + 1))
print(numbers_list)

print(numbers_list[a - 1] * numbers_list[b - 1])
