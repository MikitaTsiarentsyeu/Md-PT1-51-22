for i in range(1, 101):
    res = ""
    if i % 3 == 0:
        res += "FIZZ"
    if i % 5 == 0:
        res += "BUZZ"
    if not res:
        res = i
    print(res, end=' ')

print('')

for i in range(1, 101):
    print((("FIZZ"*(i % 3 == 0))+("BUZZ"*(i % 5 == 0)) or i), end=' ')

