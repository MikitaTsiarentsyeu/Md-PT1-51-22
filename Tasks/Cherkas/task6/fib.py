def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-2)+fib(n-1)



while True:
    n = int(input('Enter your Fibonacci number: \n'))
    if n<=0:
        continue
    break
l = []
for i in range(1, n+1):
    l.append(fib(i))
print(l)

