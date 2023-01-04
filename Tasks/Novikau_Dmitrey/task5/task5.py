s = 'The quick Brown Fox'
def check_str(string):
    low = 0
    up = 0
    for i in string:
        if i.islower():
            low += 1
        elif i.isupper():
            up += 1
    return(up, "upper case", low, "lower case")

print(check_str(s))

def is_prime(a):
    for i in range(2, a):
        if a % i == 0: return False
    return True

a = int(input("Enter a number: "))
print(is_prime(a))


def get_ranges(list):
    m = [] 
    for i in range(len(list)-1):
        if list[i+1] == list[i]+1 and list[i-1] != list[i]-1:
            m.append(str(list[i]))
            m.append('-')
        elif list[i+1] != list[i]+1 and list[i-1] == list[i]-1:
            m.append(str(list[i]))
            m.append(',')
        elif list[i+1] != list[i]+1 and list[i-1] != list[i]-1:
            m.append(str(list[i]))
            m.append(',')
    m.append(str(list[-1]))
    return ''.join((m))
     
list = [0, 1, 2, 3, 4, 7, 8, 10]
print(get_ranges(list))



