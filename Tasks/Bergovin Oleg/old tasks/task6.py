"""1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34

2. Написать рекурсивную функцию для вычисления n первых чисел Фибоначчи. Результатом должен быть список с числами.
Примеры вызова: 
fib(5) -> [0,1,1,2,3]
fib(10) -> [0,1,1,2,3,5,8,13,21,34]"""

def sum(array):
    if not array:
        return 0

    if isinstance(array[0], list):
        return sum(array[0]) + sum(array[1:])
    return array[0] + sum(array[1:])

print(sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def fib(n, _list = [0, 1, 1]):
    if n < len(_list):
        return _list
    if len(_list) < n:
        _list.append(_list[len(_list)-1] + _list[len(_list)-2])
        fib(n, _list)
    return _list

print(fib(5))
print(fib(10))