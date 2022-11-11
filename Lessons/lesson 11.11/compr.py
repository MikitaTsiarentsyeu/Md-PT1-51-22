# l = []
# for i in range(1, 11):
#     if i%2>0:
#       l.append(i)

l = [i for i in range(1,11)]

print(l)

print([i*i for i in l])
print([print(str(i*i)) for i in l])

print([i*i for i in l if i % 2])

print([i for i in range(1, 101) if i%3==0 if i%5==0])

l = [[1,2,3], [4,5,6], [7,8,9]]
print([y for x in l for y in x])
# for x in l:
#     for y in x:
#         print(y)

d = {x:str(x) for x in range(1, 11)}
print(d)



s = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
s = list(set([{"five":5, "thirteen":13, "two":2, "eleven":11, "seventeen":17, "one":1, "ten":10, "four":4, "eight":8, "nineteen":19}[s] for s in s.split()]))
print(s)