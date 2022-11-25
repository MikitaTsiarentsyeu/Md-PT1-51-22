
def evaluate(arg1, arg2, arg3):
    res = arg1+arg2*arg3
    return res

print(evaluate(arg2=1,arg1=2,arg3=3))
print(evaluate(1,arg3=2,arg2=3))

def choose_pet_name(name_one, name_two="Good boy"):
    print(f"Choose between {name_one} and {name_two}")

choose_pet_name("Barsik", "Hunter")

def my_print(x, sep=' ', end='\n'):
    print(x, sep=sep, end=end)

my_print("test")

def calc(a, b, sign="+"):
    if sign == "+":
        return a+b
    elif sign == '*':
        return a*b

calc(2, 3)
calc(2, 3, "*")

def sum(list):
    res = 0
    for i in list:
        res += i
    return res

def sum(*args):
    res = args[0]
    skip = True
    for i in args:
        if skip:
            skip = False
            continue
        res += i
    return res

print(sum(1,2,3,4,5))

list = ['t', 'e', 's', 't']
print(sum(*list))

def my_print(arg1, *args, arg2="default value"):
    print(arg1, args, arg2)

my_print(1,2,3,4,5,6,7,8,arg2="test")
my_print(1,2,3,4,5,6,7,8)


def sum(**kwargs):
    print(kwargs, type(kwargs))

sum(arg1=1,arg2=2,arg3=3,arg4=4,arg5=5)

def my_print(*args, **kwargs):
    if 'sep' in kwargs and 'end' in kwargs:
        print(*args, sep=kwargs['sep'], end=kwargs['end'])
    else:
        print(*args)

my_print(1,2,3,4,5)
my_print(1,2,3,4,5,6,7,8,9,sep=";",end=".\n")

def calling_pets(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} the {v}")

calling_pets(kitty="cat", pit="dog")

# d = {"Zephyrka": "dog", 144:"test"}
# calling_pets(**d) error
