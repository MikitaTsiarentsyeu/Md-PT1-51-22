# merge-sort

def merge_sort(list):
    if len(list) == 1:
        return list
    middle = len(list)//2
    list1 = merge_sort(list[:middle])
    list2 = merge_sort(list[middle:])
    return merge(list1, list2)

def merge(list1, list2):
    list3 = []
    l1 = len(list1)
    l2 = len(list2)

    i, j = 0, 0

    while i < l1 and j < l2:
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    if i<l1:
        list3 += list1[i:]
    else:
        list3 += list2[j:]
    return list3


print(merge_sort([1,6,4,8,5,3,66,43,-32,0,0]))
