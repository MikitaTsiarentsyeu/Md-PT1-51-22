def reverse(new_string):
    if len(new_string) == 1:
        return new_string
    else:
        return new_string[-1] + reverse(new_string[:-1])

user_string1 = "hello"
user_string2 = "it\'s me"
print(reverse(user_string1))
print(reverse(user_string2))

def mergeSort(user_list):
    if len(user_list) > 1:
        mid = len(user_list) // 2
        left = user_list[:mid]
        right = user_list[mid:]

        mergeSort(left)
        mergeSort(right)

        i, j, k = 0, 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              user_list[k] = left[i]
              i += 1
            else:
                user_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            user_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            user_list[k]=right[j]
            j += 1
            k += 1

user_list = [2,-3,3,17,60,15,4,52,20]
mergeSort(user_list)
print(user_list)