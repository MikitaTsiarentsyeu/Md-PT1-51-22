def reverse(s, count=0):
    if count == len(s) - 1:
        return s[count] 
    else:
        return reverse(s, count + 1) + s[count]
 

print(reverse("hello"))


def merge_sort(l1,l2): 
    res = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    while i < len(l1):
        res.append(l1[i])
        i += 1
    while j < len(l2):
        res.append(l2[j])
        j += 1
    return res


def merge(l):
    if len(l)<2:
        return l
    mid = int(len(l)/2)
    l1 = merge(l[:mid])
    l2 = merge(l[mid:])
    return merge_sort(l1,l2)

    

print(merge([45, 43, 17, 2, 5, 67, 12, 11, 4, 7, 23, 19, 49, 6]))