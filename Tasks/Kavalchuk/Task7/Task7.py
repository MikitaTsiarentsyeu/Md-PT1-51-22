import random


def my_reverse(s: str) -> str:
    """Recursive function to reverse a string"""

    if len(s) == 1:
        return s
    return s[-1] + my_reverse(s[:-1])


test = "hello"
print(my_reverse(test))


print("_____________________________________")


def merge_sort(s: list) -> list:
    """Recursive function to reverse a string"""

    if len(s) == 1:
        return s
    middle = len(s) // 2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])

    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i < len(left):
        res += left[i:]
    if j < len(right):
        res += right[j:]

    return res


def quick_sort(s: list) -> list:
    """Sort the array by using quicksort."""

    if len(s) <= 1:
        return s

    elem = s[0]
    #elem = random.choice(s)
    left = list(filter(lambda x: x < elem, s))
    right = list(filter(lambda x: x > elem, s))
    center = [i for i in s if i == elem]

    return quick_sort(left) + center + quick_sort(right)


test = [78, 41, 4, 27, 3, 27, 8, 39, 19, 34, 6, 41, 13, 52, 16]
print(merge_sort(test))
print(quick_sort(test))

