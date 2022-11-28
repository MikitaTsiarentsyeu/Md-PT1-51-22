def level1():
    print("level1 started")
    level2()
    print("level1 ended")

def level2():
    print("level2 started")
    level3()
    print("level2 ended")

def level3():
    print("level3 started")
    level4()
    print("level3 ended")

def level4():
    print("level4 started")
    print("level4 ended")

# level1()

def level(current_level = 0):
    current_level += 1
    print(f"level{current_level} started")
    if current_level < 5:
        level(current_level)
    print(f"level{current_level} ended")

# level()

def print_10_times(text, i=0):
    if i == 10:
        return
    print(text)
    print_10_times(text, i+1)

# print_10_times("recursion!")

# 1! = 1
# 2! = 2*1
# 3! = 3*2*1
# 4! = 4*3*2*1
# 5! = 5*4*3*2*1

def factorial(n):
    print(n)
    if n == 1:
        return 1
    c = factorial(n-1)
    print(c)
    return n*c
# for i in range(1,6):
#     print(factorial(i))

# print(factorial(5))


def digit_sum(n):
    if n == 0:
        return 0
    return (n%10) + digit_sum(n//10)

print(digit_sum(233))