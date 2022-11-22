import random

# List Comprehension==>
def check_str(n):
    return f"{len(([i for i in n.replace(' ','') if i.upper() == i]))} upper case,\
 {len(n.replace(' ',''))-len(([i for i in n.replace(' ','') if i.upper() == i]))} lower case"


print(check_str('The quick Brown Fox'))
print(check_str('The Brooklyn Bridge is really beautiful'))
print(check_str('Python one of the most popular language for programming'))

# написал random для генерации случайных чисел
# List Comprehension==>
def is_prime(n=random.randint(0,1000)):
    return f"True\n{n} is a simple number" if len([i for i in range(2,n) if n%i==0])==0 else f"False\n{n} is not a simple number"

print(is_prime())


# тоже добавил смуты с random, тут в одну строку не получилось))==>
def get_ranges(n):
    c1 = []
    for i in range(len(n)-1):
        if n[i]+1 == n[i+1] and n[i]-1 != n[i-1]:
            c1.append(str(n[i])+'-')
        elif n[i]+1 != n[i+1] and n[i]-1 == n[i-1]:
            c1.append(str(n[i])+',')
        elif n[i]+1 != n[i+1] and n[i]-1 != n[i-1]:
            c1.append(str(n[i])+',')
    c1.append(str(n[-1])) if n[-1]-1 == n[-2] else len(n)
    c1.append(str(n[-1])) if n[-1]-1 != n[-2] else len(n)
    return repr(''.join(c1)) if len(c1)>0  else repr(','.join(map(str,n)))


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))
print(get_ranges([random.randrange(0, 100, 1), random.randrange(0, 10, 5),3,4,5,6,random.randrange(0, 50, 10),random.randrange(0, 5, 1),
random.randrange(0, 10, 1),random.randrange(0, 10, 1),10,11,12,random.randrange(0, 10, 1),random.randrange(0, 10, 1)]))