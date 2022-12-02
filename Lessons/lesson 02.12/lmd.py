from functools import reduce

def print_sq(x):
    print(x*x)

sq = lambda x: print(x*x)
print(type(sq))
sq(2)

def cycle(l, callback):
    for i in l:
        callback(i)

cycle([1,2,3,4,5], lambda x: print(x*x))
# cycle([1,2,3,4,5], print)

sum = lambda x, y: x+y
print(sum(2,3))

test_str = "Abc Aac aaa abc ccc"
print(sorted(test_str.split()))

print(ord("A"), ord("a"))

print(sorted(test_str.split(), key=lambda x: x.lower()))
print(sorted(test_str.split(), key=str.lower))

l = [("one", 1), ("two", 2), ("three", 3)]
print(sorted(l, key=lambda x: x[1]))

d = {"one":1, "two":2, "three":3}
print(sorted(d.items(), key=lambda x: x[1]))
print(sorted(d, key=d.get))

l = [1,2,3,4,5]
mp_obj = map(print, l)
print(mp_obj)
for i in mp_obj: pass

new_l = [i for i in map(lambda x: chr(x*10), l)]
print(new_l)

print([i for i in filter(lambda x: x>3, l)])

print([i for i in map(lambda x: chr(x*10), filter(lambda x: x>3, l))])

print(reduce(lambda x, y: x+y, l))
print(reduce(lambda x, y: x if x>y else y, l))
print(reduce(lambda x, y: f"{x}-{y}", l))
"1-2"
"1-2-3"
"1-2-3-4"
"1-2-3-4-5"

l = ['1', '11', '12', '22', '2', '13', '30', '33']
print(sorted(filter(lambda x: int(x) % 2 == 0, l), key=int))