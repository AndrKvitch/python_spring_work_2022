# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты воздействия через функцию input().
a = float(input())
b = float(input())
if a != 0:
    x=(-b) / a
    print(x)
else:
    print("Условие задано неверно")

