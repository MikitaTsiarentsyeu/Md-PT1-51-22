
def sum_elem(s):
    n = 0
    for i in s:
        if isinstance(i, list):
            n += sum_elem(i)
        else:
            n += i
    return n 

print(sum_elem([1, 2, [2, 4, [[7, 9], 4, 6]]]))


def fib(n, list = [0,1]):
    if len(list) < n:
        list.append(list[len(list)-1] + list[len(list)-2])
        return fib(n, list)
    else:   
        return list
    
print(fib(5))
print(fib(10))