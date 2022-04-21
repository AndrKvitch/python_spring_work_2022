#todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

#Пример:
#mass = [1,2,17,16,30,51,2,70,3,2]
#Для числа 2 индексы двух ближайших чисел: 6 и 9
#Пример:
#mass = [1,2,17,54,30,89,2,1,6,2]
#Для числа 1 индексы двух ближайших чисел: 0 и 7
#Для числа 2 индексы двух ближайших чисел: 6 и 9


mass = [1,2,1,7,16,30,51,2,70,3,2]
nums = []
for i in range(len(mass)):
    ind = []
    num = mass[i]
    counter = mass.count(num)
    if counter > 1 and num not in nums:
        nums.append(num)
for n in nums:
    ind = []
    ind1 = mass.index(n)
    ind.append(ind1)
    for j in range(mass.count(n) - 1):
        ind1 = mass.index(n, ind1 + 1)
        ind.append(ind1)
    result_razn = -123456789
    result_index = []
    for x in range(len(ind) - 1):
        if ind[x] - ind[x + 1] > result_razn:
            result_razn = ind[x] - ind[x + 1]
            result_index = [ind[x], ind[x + 1]]
    print("Для числа", n, "индексы двух ближайших чисел", result_index)