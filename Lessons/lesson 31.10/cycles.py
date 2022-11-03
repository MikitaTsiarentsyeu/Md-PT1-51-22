# while True:
#     print("To Infinity and beyond!!!")

x = 0
while x < 10:
    x += 1
    print(x)

l = [1,2,3,4,5]
x = 0
while x < len(l):
    print(f"position - {x}, value - {l[x]}")
    x += 1

x = 0
while x < len(l)-1:
    print(f"current value - {l[x]}, next value - {l[x+1]}")
    x += 1

for x in l:
    print(x)

for x in "test":
    print(x, end=' ')

print(x)

# for i in range(len(l)):
#     print(l[i])

# for i in range(0, 21):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

start = 97
for i in range(26):
    print(chr(start+i), end=" ")
print('\n')

for i in (1,2,3,4,5):
    print(i, end=' ')
print('\n')

for i in set("some string"):
    print(i, end=' ')
print('\n')

for i in set("some string"):
    print(i, end=' ')
print('\n')

d = {1:"one", 2:"two", 3:"three"}
for i in d:
    print(f"key - {i}, value - {d[i]};", end=' ')
print('\n')

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

for i in d.values():
    print(i, end=' ')
print('\n')

for k, v in d.items():
    print(f"key - {k}, value - {v};", end=' ')
print('\n')

# l = [1]
# counter = 0
# for i in l:
#     print(counter)
#     l.append(i)
#     counter += 1

l = list(range(10))
for i in l:
    print(i)
    print(l.pop())

for i, e in enumerate("test string"):
    print(i, e, end=' ')
print('\n')

l = [[1,2,3], [4,5,6], [7,8,9]]
for i in l:
    for j in i:
        print(j)

