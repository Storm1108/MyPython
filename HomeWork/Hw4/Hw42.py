# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# in
# 54
# out
# [2, 3, 3, 3]
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
# in
# 650
# out
# [2, 5, 5, 13]
def Simple_List(n):
    simples = []
    check = 0
    for i in range(2, n):
        for j in range(2, i // 2 + 1):
            if (i % j) == 0:
                check = 1
                break
        if check == 0:
            simples.append(i)
        check = 0
    return tuple(simples)


def Simple_Multiplicators(n):
    simples = Simple_List(n // 2 + 1)
    multiplicators = [1]
    i = 0
    while i < len(simples):
        if (n % simples[i]) == 0:
            multiplicators.append(simples[i])
            n = n // simples[i]
            i -= 1
        i += 1
    if len(multiplicators) == 1:
        multiplicators.append(n)
    return multiplicators


print(Simple_Multiplicators(int(input("Введите целое число: "))))
