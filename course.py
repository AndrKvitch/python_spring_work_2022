#todo: I вариант (алгоритм сортировки вставками)
#Реализовать на Python алгоритм сортировки вставками представленный в псевдокоде
#в учебнике “Introduction to Algorithms”  на стр. 57 - 63.

### Алгоритм сортировки: ###
#def insertion_sort(a):
#    for j in range(1, len(a)):
#        key = a[j]
#        i = j - 1
#        while i >= 0 and a[i] > key:
#           a[i + 1] = a[i]
#            i -= 1
#        a[i + 1] = key
#    return a
from helpers import insertion_sort
a = [7, 5, 8, 11, 4, 2]

print(insertion_sort.insertion_sort(a))
