#todo:Создайте программу, которая будет выводить все возможные комбинации при броске 2 игральных костей
#и сумму их значений. У игральной кости стороны пронумерованы от 1 до 6.

#Пример вывода:
#Сумма 2   комбинация [(1,1)]
#Сумма 3   комбинация [(1,2),(2,1)]
#Сумма 4   комбинация [(1,3),(3,1),(2,2)]
#........................................
#Выводы комбинаций оформить в список кортежей.


print("Введите сумму")
a = int(input())
t = []
if a == 2:
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == 2:
                t.append((i, j))
    print("Cумма 2 комбинация", t)
if a == 3:
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == 3:
                t.append((i, j))
    print("Cумма 3 комбинация", t)
if a == 4:
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == 4:
                t.append((i, j))
    print("Cумма 4 комбинация", t)
if a == 5:
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == 6:
                t.append((i, j))
    print("Cумма 5 комбинация", t)
if a == 6:
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == 6:
                t.append((i, j))
    print("Cумма 6 комбинация", t)
if a == 7:
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == 7:
                t.append((i, j))
    print("Cумма 7 комбинация", t)
if a == 8:
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == 8:
                t.append((i, j))
    print("Cумма 8 комбинация", t)
if a == 9:
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == 9:
                t.append((i, j))
    print("Cумма 9 комбинация", t)
if a == 10:
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == 10:
                t.append((i, j))
    print("Cумма 10 комбинация", t)
if a == 11:
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == 11:
                t.append((i, j))
    print("Cумма 11 комбинация", t)
if a == 12:
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == 12:
                t.append((i, j))
    print("Cумма 12 комбинация", t)
