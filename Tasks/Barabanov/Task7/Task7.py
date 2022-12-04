#1. Написать рекурсивную функцию для разворота строки, используя только конкатенацию.
#reverse("hello") => "olleh"

st = "hello"
def reverse(st):
    str = "".join(reversed(st))
    return str

print("Reversed string is :", reverse(st))

# example 2

st = "hello"


def reverse(st):
    if len(st) == 0:
        return st
    else:
        return reverse(st[1:]) + st[0]


print("Reversed string is :", reverse(st))

#2. Изучить принцип работы алгоритма сортировки слиянием (merge sort) или быстрой сортировки (quicksort) на выбор, описать его в виде рекурсивной функции.

import operator
def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

array = [13, 5, 96, 74, 8, 24, 2, 33, 44, 56, 1, 15, 47, 3, 65, 11]
merge_sort(array)
print(merge_sort(array))