l = [1,2,3,4,5,[1,2,3, [1,2,3]],6]

def sum_num(li):
    sum = 0
    for i in li:
        if type(i) != list:
            sum+=i
        elif type(i) == list:
            sum += sum_num(i)
    return(sum)
    
print(sum_num(l))



def fibonacci(n):
    if n ==1 or n==0:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

def create_fib_list(n, l =[]):
    for i in range(n):
        l.append(fibonacci(i))
    return l

print(create_fib_list(7))
