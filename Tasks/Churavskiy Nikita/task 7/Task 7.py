def reverseString(some_string):
   return some_string if some_string == "" else reverseString(some_string[1:]) + some_string[:1]

print(reverseString('hello'))


def merge_two_list(a,b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i]<b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    if i < len(a):
        result += a[i:]
    if j < len(b):
        result += (b[j:])
    return result


def merge_sort(s):
    if len(s) == 1:
        return s
    middle = len(s)//2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_list(left, right)

print(merge_sort([9,5,6,7,8,4,3,5]))
