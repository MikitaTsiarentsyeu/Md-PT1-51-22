
def GetSumElem(lst: list):
    sum = 0
    for i in lst:
        if type(i) is list:
            sum += GetSumElem(i)
        else:
            sum += i
    return sum 

print(GetSumElem([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def GetFibonacci(n: int, list = [0, 1]) -> list:
    if len(list) < n:
        list.append(list[len(list)-2] + list[len(list)-1])
        GetFibonacci(n, list)
    return list

print(GetFibonacci(12))

