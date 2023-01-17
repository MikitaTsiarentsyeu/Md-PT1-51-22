def sum_mas(list):
    mysum = 0
    for el in list:
        if (type(el) == type ([])):
            mysum = mysum + sum_mas(el)
        else:
            mysum = mysum + el
    return mysum

list = [1,2,3, [3,4,5,[4,5,6,[7,8,[1],9],7],6],5]
print("Sum of elements:", sum_mas(list))

def fibo(n):
    if n == 2:
        return [0, 1]
    lst = fibo(n - 1)
    lst.append(lst[-1] + lst[-2])
    return lst 
 
print("fib(10) ->", fibo(10))