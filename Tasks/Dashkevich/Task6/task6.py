def list_sum(elem):
    sum = 0
    for i in elem:
        if not isinstance(i, list):
            sum += i
        else:
            sum += list_sum(i)     
    return sum

list_example1 = [1, 2, [2, 4, [[7, 8], 4, 6]]]
list_example2 = [ -2, 3, 8, 11, [-4, 6, [ 2, [-5, 4] ] ] ]
print("Sum:", list_sum(list_example1))
print("Sum:", list_sum(list_example2))


def fibonacci(n: int) -> int:
    "Function for count Fibonacci numbers"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        return result

def fibonacci_list(numb: int) -> list:
    "Function for adding Fibonacci numbers in list"
    l = []
    for number in range(0, numb):
        l.append(fibonacci(number))
    return  list(l)

print(fibonacci_list(5))
print(fibonacci_list(10))