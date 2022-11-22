from word2number import w2n


l = []

for i in "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split(" "):
    i = w2n.word_to_num(i)
    l.append(i)

l = list(set(l))
print(l)
l.append(0)

for i in range(len(l)-1):
    if i % 2 == 0:
        if i <= (len(l) - 2):
            print(l[i] * l[i + 1])
        if i <= (len(l) - 4):
            print(l[i + 1] + l[i + 2])
    if l[i] % 2 != 0:
        l[-1] += l[i]
print(f"сумма нечетных чисел:", l[-1])

