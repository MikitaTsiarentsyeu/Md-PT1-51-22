
def check_str(x):  
    counter = 0
    for n in x:
        if n.isupper():
            counter += 1
    return f'{counter} upper case, {len("".join(x.split())) - counter} lower case'

print(check_str("The quick Brown Fox"))


def is_prime(x):    
    for n in range(2, (x//2)+1):
        if x%n == 0:
            return False
    return True

print(is_prime(787))
print(is_prime(777))


def get_ranges(x):
    l = []
    for i in range(len(x)-1):
        if x[i]+1 == x[i+1] and x[i]-1 != x[i-1]:
            l.append(str(x[i])+'-')
        elif x[i]+1 != x[i+1] and x[i]-1 == x[i-1]:
            l.append(str(x[i])+','+' ')
        elif x[i]+1 != x[i+1] and x[i]-1 != x[i-1]:
            l.append(str(x[i])+','+' ')
    l.append(str(x[-1]))          
    return "".join(l)

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))