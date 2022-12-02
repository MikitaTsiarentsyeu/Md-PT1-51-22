# 1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34
result_sum = 0

def count_values(list):
    global result_sum
    for i in list:
        if type(i) == int:
            result_sum += i
        else:
            count_values(i)
    return result_sum

print("Subtask 1:\n", count_values([1, 2, [2, 4, [[7, 8], 4, 6]]]))

# 2. Написать рекурсивную функцию для вычисления n первых чисел Фибоначчи. Результатом должен быть список с числами.
# Примеры вызова:
# fib(5) -> [0,1,1,2,3]
# fib(10) -> [0,1,1,2,3,5,8,13,21,34]

def fib(n):
    if n == 2:
        return [0, 1]
    lst = fib(n - 1)
    lst.append(lst[-1] + lst[-2])
    return lst

print("Subtask 2:")
print(fib(5))
print(fib(10))
