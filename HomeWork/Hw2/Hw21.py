# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
numberStr = input("Enter number: ")
length = len(numberStr)
number = float(numberStr)
number *= 10 ** (length - 1)
summ = 0
for i in range(length):
    summ = summ + int(number % 10)
    number //= 10
print("Character sum: ", summ)
