def sum_elem(l):
    return sum([i if type(i) == int else sum_elem(i) for i in l])
l = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print(sum_elem(l))