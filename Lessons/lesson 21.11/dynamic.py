# def add(a, b):
#     return a+b

# def add(a, b, c):
#     return add(add(a, b), c)

# add(2,3,4) functional polymorphis 

def add_two(a, b):
    return a+b

def add_three(a, b, c):
    return add_two(add_two(a, b), c)

print(add_three(2,3,4))



def times(a:object, b:object) -> object:
    return a*b

print(times(2, 3))
print(times("test", 4))

def times_for_int(a:int, b:int) -> int:
    "this function will multiply only int values"
    if isinstance(a, int) and isinstance(b, int):
        return a*b

print(times_for_int(2, 3))
print(times_for_int("test", 4))

def eq(l1, l2):
    for i in l1:
        if i not in l2:
            return False
    for i in l2:
        if i not in l1:
            return False
    return True

print(eq([1,2,3], (3,2,1)))
print(eq("321", ['2','3','1']))
    