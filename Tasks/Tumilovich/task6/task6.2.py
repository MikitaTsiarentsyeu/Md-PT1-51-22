def fibo_list(n):
    if n == 2:
        return [0,1]
    list = fibo_list(n-1)
    list.append(list[-1] + list[-2])
    return list
print(fibo_list(10))

