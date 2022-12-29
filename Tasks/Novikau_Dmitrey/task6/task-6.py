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
    
    if n in (1,2):
        return 1
    return fibo(n-1) + fibo(n-2)
    
 
print("fib(10) ->", fibo(10))


#2. Написать рекурсивную функцию для вычисления n первых чисел Фибоначчи. Результатом должен быть список с числами.
#Примеры вызова: 
#fib(5) -> [0,1,1,2,3]
#fib(10) -> [0,1,1,2,3,5,8,13,21,34]
