def reverse(n):
    if len(n)==1:
        return n[0]
    else:
        return (n[-1]) + reverse(n[0:-1])

print(reverse('12456'))


def quick_sort(arr):
    if len(arr) <=1:
        return arr
    else:
        l = arr[0]
        left = list(filter(lambda x: x< arr[0], arr))
        center = [i for i in arr if i == l]
        right = list(filter(lambda x: x> arr[0], arr))
        return quick_sort(left) + center + quick_sort(right)

arr = [7,4,8,9,12,3,5]
print(quick_sort(arr))