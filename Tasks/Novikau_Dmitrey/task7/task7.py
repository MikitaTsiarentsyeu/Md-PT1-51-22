#1. Написать рекурсивную функцию для разворота строки, используя только конкатенацию.
#reverse("hello") => "olleh"

def rev(var):
    if len(var) == 1:
        return var
    return var[-1] + rev(var[:-1])
    n = str[::-1]
n = "hello"
print(rev(n))

#2. Изучить принцип работы алгоритма сортировки слиянием (merge sort) или быстрой сортировки (quicksort) на выбор,
#описать его в виде рекурсивной функции.

import random
def quicksort(a):
    if len(a) > 1:
        x = a[random.randint(0, len(a)-1)]
        less = [u for u in a if u < x]
        pivot = [u for u in a if u == x]
        greater = [u for u in a if u > x]
        a = quicksort(less) + pivot + quicksort(greater)

    return a

a = [46,32,8,5,2,78]
print(quicksort(a))