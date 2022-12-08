def reverse(l, counter = 0, res = ""):
    if counter == len(l):
        return res
    res += f"{l[len(l) - counter-1]}"
    return reverse(l, counter+1, res)


l = "hello"
print(reverse(l))
