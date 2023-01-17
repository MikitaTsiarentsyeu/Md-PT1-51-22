# recursive quick-sort
def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    elem = arr[0]
    left_side = [i for i in arr if i < elem]
    center = [i for i in arr if i == elem]
    right_side = [i for i in arr if i > elem]
    return quick_sort(left_side) + center + quick_sort(right_side)

print(quick_sort([2,6,4,9,33,7,33,2, 89, 0 ,-2]))