# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём
# X ≠  0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coodrinate: "))
if (x > 0 and y >0):
    print("1 quater")
elif (x>0 and y<0):
    print("4 quater")
elif (x < 0 and y < 0):
    print("3 quater")
elif (x< 0 and y > 0):
    print("2 quater")
elif (y == 0):
    print("Point is on axis OX")
elif (x == 0):
    print("Point is on axis OY")
