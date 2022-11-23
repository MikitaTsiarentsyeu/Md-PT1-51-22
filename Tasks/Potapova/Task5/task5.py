# TASK 1
import re

def check_str(s: str):
    s = re.sub('[^A-Za-zА-Яа-я]+', '', s)
    s1 = re.sub('[A-ZА-Я]+', '', s)
    return f'{len(s)-len(s1)} upper case, {len(s1)} lower case'


print(check_str('The quick Brown Fox'))


# TASK 2
def is_prime(num: int):
    if num == 1:
        return False
    return True not in [num % i == 0 for i in range(2, round(num**(0.5)+1))]


print(is_prime(787))
print(is_prime(777))


# TASK 3
def get_ranges(l: list):
    new_l = str(l[0])
    for pos in range(len(l)-1):
        if l[pos + 1] != l[pos] + 1 and str(l[pos]) == new_l[-1]:
            new_l = f'{new_l}, {str(l[pos + 1])}'
        elif l[pos + 1] != l[pos] + 1 and pos != len(l)-1:
            new_l = f'{new_l}-{str(l[pos])}, {str(l[pos + 1])}'
        elif l[pos + 1] == l[pos] + 1 and pos+1 == len(l)-1:
            new_l = f'{new_l}-{str(l[pos + 1])}'
    return new_l

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))
