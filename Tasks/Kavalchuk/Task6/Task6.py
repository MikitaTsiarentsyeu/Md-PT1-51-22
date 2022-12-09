def flatten(item_list: list) -> int:
    "Recursively counts and returns sum of leaf elements in (potentially nested) list."

    s = 0
    for item in item_list:
        if isinstance(item, list):
            s += flatten(item)
        else:
            s += item

    return s


line = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print(flatten(line))

print("____________________________________________")


# # Version 1

def fib_sequence(n: int) -> list:
    "Function to display the Fibonacci sequence"
    fib_numbers = [fib(i) for i in range(1, n + 1)]

    return fib_numbers


def fib(n: int, l: list = []) -> int:
    "Function for calculating the n-th element of the Fibonacci sequence"
    if n <= 2:
        return n-1
    l.append(n-1)

    return fib(n-1) + fib(n-2)

# print(fib(5))
print(fib_sequence(5))

print("____________________________________________")


# Version 2

def fibonaci(n: int, previous_value: int = 0, present_value: int = 1, fib_sequence: list = []):
    "Function to display the Fibonacci sequence"

    if n == 0:
        return fib_sequence
    fib_sequence.append(previous_value)
    if n == 1:
        return fib_sequence
    return fibonaci(n - 1, present_value, previous_value + present_value, fib_sequence)


print(fibonaci(950))

