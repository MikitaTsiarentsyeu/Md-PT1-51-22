s = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"

s = list(set(s.split()))
print(s)

s.append(0)
while True:
    if isinstance(s[s[-1]], int):
        break
    s.insert(0, {"five":5, "thirteen":13, "two":2, "eleven":11, "seventeen":17, "one":1, "ten":10, "four":4, "eight":8, "nineteen":19}[s[s[-1]]])
    s[-1] += 2

s = sorted(s[:(s[-1]//2)])
print(s)
