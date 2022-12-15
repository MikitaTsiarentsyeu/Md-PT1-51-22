def merge_two_list(a,b):
    combined_list = []
    begin_a = 0
    begin_b = 0
    while begin_a < len(a) and begin_b < len(b):
        if a[begin_a] < b[begin_b]:
            combined_list.append(a[begin_a])
            begin_a += 1
        else:
            combined_list.append(b[begin_b])
            begin_b += 1


    if begin_a < len(a):
        combined_list += a[begin_a:]
    if begin_b < len(b):
        combined_list += b[begin_b:]
    return combined_list



def merge_sort(s):
    if len(s) == 1:
        return s
    midle = len(s)//2
    left = merge_sort(s[:midle])
    right = merge_sort(s[midle:])
    return merge_two_list(left,  right)


s = [7, 5, 2, 3, 9, 8, 6]
print(merge_sort(s))

