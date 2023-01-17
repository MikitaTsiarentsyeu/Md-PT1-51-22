def check_num(n):
    while True:
        if isinstance(n, int):
            break
        if not n.isdigit() or int(n) == 0:
            print('The number must be numeric and >0')
            n = input()
            continue
        break
    return n

def is_prime(n):
    n = check_num(n)
    for i in range(2, int(int(n)**0.5)+1):
        if int(n) % i == 0:
            return False
    return True

n = input()
print(is_prime(n))

print(is_prime(777))
print(is_prime(787))