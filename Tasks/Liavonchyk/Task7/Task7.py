l = [2,17,1,7,4,65,65,6,3,45,17]
l1 = [2,17,1,7,4,65,65,6,3,45,17]
# quicksort
def qsort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[len(array)//2]
        less = [i for i in array[0:] if i < pivot]
        equal = [i for i in array[0:] if i == pivot]
        greater = [i for i in array[0:] if i > pivot]
        return qsort(less) + equal + qsort(greater)


def merge(array, left, right):
    i = j = k = 0 #counters

    while i < len(left) and j < len(right): # same amount check
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left): #add rests
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
    return array

# merge sort
def msort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        msort(left)
        msort(right)
        merge(array,left,right)

    return array


# Reverse line
def reverse(in_line):
    if len(in_line) < 2:
        return in_line
    new_line = str(in_line[-1]) + str(reverse(in_line[:len(in_line) - 1]))
    return new_line



print(l, qsort(l))

print(l, msort(l1))

print(reverse("This is test sting!"))