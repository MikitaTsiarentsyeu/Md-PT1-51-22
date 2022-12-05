# 1. Написать рекурсивную функцию для разворота строки, используя только конкатенацию.
# reverse("hello") => "olleh"

def reverse(s, counter=0):
    return s[counter] if counter == len(s) - 1 else reverse(s, counter + 1) + s[counter]

print(reverse("hello"))

# 2. Изучить принцип работы алгоритма сортировки слиянием (merge sort) или быстрой сортировки (quicksort) на выбор, описать его в виде рекурсивной функции.
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(l):
    if len(l) < 2:
        return l[:]
    else:
        mid = len(l) // 2
        left = merge_sort(l[:mid])
        right = merge_sort(l[mid:])
        return merge(left, right)


print(merge_sort([6, 5, 4, 9, 1, 3, 2, 5]))
