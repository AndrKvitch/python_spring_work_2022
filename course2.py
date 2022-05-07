
#Задача.
#Переверните INSERTION_SORT и отсортируйте последовательности
def insertion(a):

    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] < key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
    return a
a = [ 31 , 4 , 59 , 26 , 41 , 58 , 1 , - 20 , 100 , - 7 ]
print(insertion(a))