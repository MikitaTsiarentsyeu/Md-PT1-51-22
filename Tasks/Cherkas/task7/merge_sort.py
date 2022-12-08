def merge_two_list(a,b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if i < len(a):
        c+=a[i:]
    if j < len(b):
        c+=b[j:]

    return c


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    middle = len(lst)//2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge_two_list(left,right)

lst = [1,5,7,6,8,0,4,5,9,12]
print(merge_sort(lst))
