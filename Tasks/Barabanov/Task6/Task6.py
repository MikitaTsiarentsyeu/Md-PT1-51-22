# 1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34
# res_sum = 0

def count_val(lst):
    res_sum = 0
    for i in lst:
        res_sum += i if type(i) == int else count_val(i)
    return res_sum

print(count_val([1, 2, [2, 4, [[7, 8], 4, 6]]]))

# 2. Написать рекурсивную функцию для вычисления n первых чисел Фибоначчи. Результатом должен быть список с числами.
# Примеры вызова:
# fib(5) -> [0,1,1,2,3]
# fib(10) -> [0,1,1,2,3,5,8,13,21,34]

def fibonacci(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    list = fibonacci(n - 1)
    list.append(list[-1] + list[-2])
    return list

print(fibonacci(5))
print(fibonacci(10))

