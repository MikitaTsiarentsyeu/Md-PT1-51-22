a = [1, 2, [2, 4, [[7, 8], 4, 6]]]
def rec(l):
    sum = 0
    for i in l:     
        if type(i) == int:
             sum+=i    
        else:
            sum = sum+rec(i)
    return sum
print(rec(a))
