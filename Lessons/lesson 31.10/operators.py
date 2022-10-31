s = "some data?"

# for i in s:
#     if i in " ,.:?!": 
#         pass
#     else:
#         print(i)
# else:
#     print("hello from else")

flag = False
for i in s:
    if i in " ,.:?!":
        flag = True
    else:
        print(i)
print(flag)

counter = -1
while True:
    counter+=1
    if counter == len(s)-1:
        break
    if s[counter] in " ,.:?!":
        continue
    print(s[counter], end=' ')
else:
    print("else")
print('\n')

counter = 5
for i in s:
    if i in " ,.:?!":
        continue
    if counter <= 0:
        break
    counter -= 1
    print(i, end=' ')
else:
    print("else")