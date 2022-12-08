
def sumlist(lst):
    s=0
    for i in range(0,len(lst)):
        if type(lst[i]) == int:
            s+=lst[i]
        elif type(lst[i]) == list:
            s+=sumlist(lst[i])
    return s

#print(sumlist([1, 2, [2, 4, [[7, 8], 4, 6]]]))



def fib(n,lst):
    if len(lst)==n:
        return print(lst)
    else:
        lst.append(lst[len(lst)-2] + lst[len(lst)-1])
        fib(n,lst)

count = input("Enter digit\n")
fib(int(count),[0,1])