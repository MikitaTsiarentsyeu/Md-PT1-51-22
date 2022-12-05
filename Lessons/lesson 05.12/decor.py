def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

def comment(func):
    def wrapper():
        print("the process has began")
        func()
        print("it's done")
    return wrapper

@do_twice
@comment
def print_something():
    print("something")

# print_something = do_twice(print_something)
print_something()