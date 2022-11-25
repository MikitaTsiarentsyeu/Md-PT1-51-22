# for i in range(10):
#     i+2

l = [i for i in range(10)]

# print(i)

global_var = 10

def scope_test(global_var):
    print(global_var)
    global_var = "value from a function"
    print(global_var)

scope_test("test")
print(global_var)


def test_global():
    global global_var
    global_var = "value from test_global"
    print(global_var)

test_global()

print(global_var)


def outer_func():
    x = "outer value"
    print(x)
    def inner_func():
        nonlocal x
        print(x)
        x = "inner value"
        print(x)
    inner_func()
    print(x)

outer_func()


global_list = []

def test_global_list(x):
    global_list.append(x)

test_global_list("test")
print(global_list)