# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5
def Fibbonachi(n):
    if n > 1:
        fibb_list = [1, 0, 1]
        for i in range(1, n):
            fibb_list.insert(0, (((-1) ** i) * (fibb_list[-2] + fibb_list[-1])))
            fibb_list.append(fibb_list[-2] + fibb_list[-1])
        return fibb_list
    else:
        return [0]


print(Fibbonachi(8))
