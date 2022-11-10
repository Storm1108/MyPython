# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
# in
# 11
# out
# 1011
def Num2th(num10th):
    print(f"Число в 10-ричной системе исчисления: {num10th}")
    if ((num10th == 0) or (num10th == 1)):
        return num10th
    else:
        Parts = []
        count = 0
        while (num10th != 1):
            Parts.insert(0, num10th % 2)
            print(Parts)
            num10th = num10th // 2
            count += 1
        Parts.insert(0, 1)
        return ("".join(map(str, Parts)))


num10th = 88
print(f"Число в двоичной системе исчисления: {Num2th(num10th)}")
