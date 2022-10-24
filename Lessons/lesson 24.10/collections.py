print("LIST")

l = []
print(type(l))

print(len(l))

print(list("my test string"))
print([1,2,3]+[4,5,6])
print([0]*10)

l = [1,2,3,4,5,"six",7.0,True]
print(l)

print(l[0], l[1], l[-1])
print(l[1:7:2])
print(l[::-1])

l[0] = 1.0
print(l)

l.append("new element")
print(l)

l.insert(0, "new first element")
print(l)

# l.extend([3,4,5])
l.extend("test")
print(l)

if 't' in l:
    l.remove('t')

if 't' in l:
    l.remove('t')

if 't' in l:
    l.remove('t')

print(l)

print(l.pop())
print(l.pop())
print(l.pop())
print(l)

print(l.pop(0))
print(l.pop(0))
print(l.pop(0))
print(l)

del l[3]
print(l)

del l[1:3]
print(l)

l.clear()
print(l)

# del l
# print(l) error

l = [1,2,3]
m = [1,3,2]
print("equal" if l==m else "not equal")

l = [1,2,3,4,5,6,7,8,9,10]
# swap = l[0]
# l[0] = l[9]
# l[9] = swap
l[0], l[9] = l[9], l[0]
print(l)

l[0:3], l[4:7] = l[4:7], l[0:3]
print(l)

# l[100] index out of range error

print("TUPLE")

t = ()
print(type(t))

t = (1,)
print(type(t))

print(len(t))

t = (1,2,3,4,5,6,7,8,9,"ten",False)
print(t)

print(tuple("test"))
print(tuple([2,5,8,"test"]))

print((1,2,3)+(4,5,6), (0,)*10)

print(t[0], t[-1], t[2:7:2])

# t[0] = "new elem" error
# del t[0] error

print(t.index(False))

del t

print("DICT")

d = {}
print(type(d))

d = {"one":1, 2:"two", 3:3, "four":"four"}
print(d)

print(d["one"], d[3], d[2])

# {[]:"new list"} error

d["new_key"] = "new value"
print(d)

d["new_key"] = "the same but still new value"
print(d)

d[3] = "three"
d[3] = 3.0
d[3] = [3]
print(d)

print(d.get(33, "there is no such value"))

print(3 in d)
print(1 in d)

print(d.keys())
print(d.values())
print(d.items())

print(1 in d.values())

d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

"the result is Reina Meinhard from Memphis, Tennessee"
"nothing was found"

num = int(input("Please enter your number:\n"))

if num in d:
    data = d[num]
    print(f"the result is {data[0][1]} {data[0][0]} from {data[1][0]}, {data[1][1]}")
else:
    print("nothing was found")

data = d.get(num, False)
if data:
    print(f"the result is {data[0][1]} {data[0][0]} from {data[1][0]}, {data[1][1]}")
else:
    print("nothing was found")