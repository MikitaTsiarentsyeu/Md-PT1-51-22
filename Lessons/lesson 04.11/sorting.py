l = [2,5,4,1,3,6,9,7,8]

print(min(l))

print(sorted(l)[0])

min = l[0]
for i in l:
    if i < min:
        min = i

print(min)

print(sorted(l))
print(l)

# l.sort()
# print(l)

print(sorted([(2, "test"), (1, "lol")]))



# for i in range(len(l)-1):
#     print(l)
#     for j in range(len(l)-i-1):
#         if l[j] > l[j+1]:
#             l[j], l[j+1] = l[j+1], l[j]

# print(l)


# min = 0
# for i in range(len(l)):
#     if l[i] < l[min]:
#         min = i
# l[0], l[min] = l[min], l[0]

# print(l)

# min = 1
# for i in range(1, len(l)):
#     if l[i] < l[min]:
#         min = i
# l[1], l[min] = l[min], l[1]

# print(l)

# min = 2
# for i in range(2, len(l)):
#     if l[i] < l[min]:
#         min = i
# l[2], l[min] = l[min], l[2]

# print(l)

# min = 3
# for i in range(3, len(l)):
#     if l[i] < l[min]:
#         min = i
# l[3], l[min] = l[min], l[3]

# print(l)

for c in range(len(l)-1):
    min = c
    for i in range(c, len(l)):
        if l[i] < l[min]:
            min = i
    l[c], l[min] = l[min], l[c]

print(l)