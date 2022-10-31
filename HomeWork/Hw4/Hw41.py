# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000
def Accuracy(d):
    i = 0
    while d != 1:
        d *= 10
        i += 1
    return int(i)


a = float(input("Enter a real number:"))
d = float(input("Enter the required accuracy '0.0001':"))
print(f"%.{Accuracy(d)}f" % a)
