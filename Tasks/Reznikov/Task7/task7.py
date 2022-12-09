import random

"""1. Написать рекурсивную функцию для разворота строки, используя только конкатенацию.
reverse("hello") => "olleh"

2. Изучить принцип работы алгоритма сортировки слиянием (merge sort) или быстрой сортировки (quicksort) на выбор, описать его в виде рекурсивной функции."""

def reverse(str):
    if len(str) == 0:
        return str
    return str[-1] + reverse(str[:-1])

print(reverse('hello'))

def quicksort(array):
    if len(array) < 2:
        return array

    sup = array[random.randint(0, len(array)-1)]
    
    left = [i for i in array if i < sup]
    right = [i for i in array if i > sup]
    return quicksort(left) + [sup] + quicksort(right)

print(quicksort([1,7,3,8,9,22,6,11,15,12,47,40,32]))


def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i,j,k = 0,0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i = i+1
        else:
            array[k] = right[j]
            j = j+1
        k = k+1

    while i < len(left):
        array[k] = left[i]
        i = i+1
        k = k+1

    while j < len(right):
        array[k] = right[j]
        j = j+1
        k = k+1
    return array


print(merge_sort([1,7,3,8,9,22,6,11,15,12,47,40,32]))
