# todo: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A,
# и вывести новые значения переменных A, B, C.

a=float(input())
b=float(input())
c=float(input())
task1=b
task2=c
c=a
a=task1
b=task2

print(a, b, c)