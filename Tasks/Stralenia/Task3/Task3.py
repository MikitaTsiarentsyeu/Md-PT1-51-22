d = {"one":1,
"two":2,
"three":3,
"four":4,
"five":5,
"six":6,
"seven":7,
"eight":8,
"nine":9,
"ten":10,
"eleven":11,
"twelve":12,
"thirteen":13,
"fourteen":14,
"fifteen":15,
"sixteen":16,
"seventeen":17,
"eightteen":18,
"nineteen":19,
"twenty":20}


x = [d[k] for k in input("Enter your number from 1 to 20:\n").split()]

print (sorted(list(set(x))))

for i in range(len(sorted(list(set(x))))-1):
    if i%2 > 0:
        res = (sorted(list(set(x))))[i] + (sorted(list(set(x))))[i+1]
    else:
        res = (sorted(list(set(x))))[i] * (sorted(list(set(x))))[i+1]
    print (res, end=' ')
print ('\n')        


for e in sorted(list(set(x))):
    if e%2 > 0:
        sum = 0 + e
print (sum)
print ('\n')


