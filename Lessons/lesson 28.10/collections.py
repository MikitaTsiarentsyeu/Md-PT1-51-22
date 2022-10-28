
l = [1,2,3,4,5,6.0,"test"]
l.append("new elem")

t = (1,2,3,4,5,"some string")
# t.append()

d = {"test":"some value", (1,2,3,4,5):"tuple value"}
d["test"] = "new value"

s = set()
print(s, type(s))

s = {1}
print(s, type(s))

s = {1,2,3,4,5}
print(s)

s = {1,2,3,4,5,"test",(1,2,3,4,5)}
print(s)

s = {1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3}
print(s)

print(set("test"))

s = set("some test string")
print(s)

l = [1,1,1,2,2,3,3,4,4,5,5,6,6,7]
l = list(set(l))

l = list("aaabbbbccccddddeeeeffffgggg")
print(l)
l = list(set(l))
print(l)

l1 = [1,2,3,3,3,3,3,3,3,3]
l2 = [3,2,1]
print(l1==l2, set(l1)==set(l2))

# {1,2,3,4,5,["test"]} error

s = {1,2,3,4,5}
s.add(1)
s.add(6)
print(s)

s.update([4,5,6,7,8,9])
print(s)

s.update("test string to add into set")
print(s)

# s.add([]) error

# s.update([[]]) error

s.remove(1)
print(s)

# s.remove(1) error
# print(s)

s.discard(1)
# if 1 in s: the same as discard
#     s.remove(1)


print({1,2,3}.union({3,4,5}))
print({1,2,3}.intersection({3,4,5}))

print({1,2,3}.issubset({1,2,3,4,5,6}))

