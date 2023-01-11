
def reverse(sting):
    if len(sting) == 1:
        return sting
    else:
        return reverse(sting[1:]) + sting[0]

sting = "hello"
print(reverse(sting))


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

print(merge_sort([6, 5, 4, 9, 1, 3, 2, 7, 8]))