# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
n = int(input("Enter N: "))
number_list = []
for i in range(1, n+1):
    number_list.append(round((1 + 1 / i) ** i))
print(number_list)