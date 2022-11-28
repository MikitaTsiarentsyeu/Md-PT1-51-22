storage = 0

def counter(n):
    def action():
        nonlocal n
        n+=1
        return n
    return action

from_10 = counter(10)
print(from_10())
print(from_10())
print(from_10())
print(from_10())

from_100 = counter(100)
print(from_100())
print(from_100())
print(from_100())
print(from_10())