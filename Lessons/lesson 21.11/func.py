
# print(my_sum(2,3,4))

def my_sum(a, b, c):
    res = a+b+c
    return res

print(my_sum(2,3,4))
print(my_sum(3,3,3))

def add_number(x, is_list):
    print(id(x))
    if is_list:
        x[0] += 2
    else:
        x += 2
    print(x)
    print(id(x))
    return x

test_number = 5
test_list = [5]

print(id(test_number))
test_number = add_number(test_number, False)
print(test_number)

print(id(test_list))
add_number(test_list, True)
print(test_list)

[1,2,3].sort()

sorted([1,2,3])


def print_param_value(val1, val2, val3):
    print(val1, val2, val3, sep="-", end=";\n")

x = print_param_value("cat", "dog", "cat")
print(x)

def operation(x, y, sign):
    if sign == "+":
        return x+y
    elif sign == "*":
        return x*y
    # else:
    #     return


print(operation(2, 3, '+'))
print(operation(2, 3, '*'))
print(operation(2, 3, '-'))

def get_None():
    return

def canonical_mult(a, b):
    if b < 0:
        a = -a
        b = -b
    res = 0
    for i in range(b):
        res += a
    return res

print(canonical_mult(2, 3))
print(canonical_mult(2, 0))
print(canonical_mult(-2, -3))