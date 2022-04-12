# todo:  Даны три переменные: X, Y, Z. Их значения числа.
# Из данных произвольных чисел выбрать наибольшее.

x = int(input())
y = int(input())
z = int(input())
if x > y and x > z:
    print("Наибольшее число", x)
elif y > x and y > z:
    print("Наибольшее число", y)
elif z > x and z > y:
    print("Наибольшее число", z)