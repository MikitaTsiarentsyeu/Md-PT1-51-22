def summ_all (l):
    summ = 0

    for i in l:
        if not isinstance(i, list):
            summ = summ + i
        else:
            summ = summ + summ_all(i)
    return summ


l = [1, 2, [2, 4, [[7, 8], 4, 6]]]

summ = summ_all(l)

print(f"summ_all = {summ}")

