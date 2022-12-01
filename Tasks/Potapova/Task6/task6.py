# TASK 1
def summ(spis: list) -> int:
    total = 0
    for val in spis:
        if isinstance(val, list):
            total = total + summ(val)
        else:
            total = total + val
    return total

print(summ([1, 2, [2, 4, [[7, 8], 4, 6]]]))



# TASK 2 VAR_1 without recursion
# def fib_numbers(num: int) -> list:
#     spis = [0, 1]
#     for val in range(2, num):
#         spis.append(spis[-1]+spis[-2])
#     return spis



# VAR_2
def fib_numbers(num: int) -> list:
    if num <= 2:
        return [0, 1]
    else:
        spis = fib_numbers(num-1)
        spis.append(spis[-1]+spis[-2])
    return spis

print(fib_numbers(5))


