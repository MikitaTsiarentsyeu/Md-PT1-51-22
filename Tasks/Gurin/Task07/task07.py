def getReverseStr(str, counter = 0, res=''):
    if counter == len(str):
        return res
    res = f'{res+str[len(str)-1 - counter]}'
    return getReverseStr(str, counter+1, res)

print(getReverseStr("hello world"))  

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j +=1 
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j +=1
            k += 1

my_list = [6, 7, 9, 1, 66, 43, 2]
mergeSort(my_list)
print(my_list)