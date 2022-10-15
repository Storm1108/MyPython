# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input("Enter N: "))
number_list = [1]
for i in range(1, n+1):
    number_list.append(number_list[i-1] * i)
print(number_list)