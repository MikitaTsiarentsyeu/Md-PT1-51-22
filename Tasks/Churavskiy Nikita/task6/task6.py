
# sum digits in list
def some_func(s):
    return s if s == [] else (some_func(s[0]) + some_func(s[1:])) if isinstance(s[0], list) else (s[:1] + some_func(s[1:]))


print(f"сумма всех элементов - {sum(some_func([1, 2, [2, 4, [[7, 8], 4, 6]]]))}")
print(f"сумма всех элементов - {sum(some_func([3, 5, [6,[1,[2]], 4, [[7,[1], 8,[40]], 4, 6]]]))}")


# fibonacci
def fibonacci(n):
    return n if n <= 1 else (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Введите число членов последовательности:"))
c = [fibonacci(i) for i in range(n)]


print(f"fib({n})-->{c}")
 










