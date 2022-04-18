#todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

#Пример:
#mass = [1,2,17,16,30,51,2,70,3,2]
#Для числа 2 индексы двух ближайших чисел: 6 и 9
#Пример:
#mass = [1,2,17,54,30,89,2,1,6,2]
#Для числа 1 индексы двух ближайших чисел: 0 и 7
#Для числа 2 индексы двух ближайших чисел: 6 и 9


mass = [1,2,1,7,16,30,51,2,70,3,2]

for i in mass:
    if mass.count(i) > 1:
        x = i
y = []
z = []

if x in mass:
    counter = 0
    start = 0
    if mass.count(x) == 1:
        print("В массиве одно значение, под индексом :", x)
    else:
        while counter < mass.count(x):
            start = mass.index(x, start, len(mass)) +1
            counter += 1
            y.append(start - 1)
else:
    print("No massive")

for j in range(0, len(y)-1):
    z.append(y[j + 1] - y[j])

for j in range(0, len(y) - 1):
    if y[j + 1] - y[j] == min(z):
        print("Для числа", i, "индексы двух ближайших чисел:", y[j], "и", y[i])
