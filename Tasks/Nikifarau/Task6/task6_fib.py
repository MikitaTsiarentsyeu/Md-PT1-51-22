def create_fib(n):
    global l
    longd = len(l)

    begin_fib = l[-2]
    end_fib = l[-1]

    if longd < n:
        l = l + [begin_fib + end_fib]
        return create_fib(n)
    else:
        return l


l = [1, 2]

print(f" look for list Fibonachi (5): {create_fib(5)}")
print(f" look for list Fibonachi (10): {create_fib(10)}")
