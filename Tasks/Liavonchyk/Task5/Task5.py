import math

def check_str(str_in):
    count_up = 0 # initialize
    count_low = 0
    for letter in str_in:
        if letter.isalpha():  # we explicitly check alpabetical values
            if letter.isupper():
                count_up += 1
            else:
                count_low += 1

    return f'{count_up} upper case, {count_low} lower case'

def is_prime(num):
    if num > 0: # positive
        if num == 1: # 1 is not prime or composite
            return 'THIS IS OOOOONE!!!!!'
        if num == 2: # 2 is even and prime
           return True
        if num % 2 == 0: # if number is even and != 2 it is composite
            return False
        lim = int(math.sqrt(num)) + 1  # find the limit to stop checking
        for i in range(3, lim + 1, 2): # we will check only odd numbers with step 2
            if num % i == 0:
                return False
    else:
        return 'Number must be > 0'
    return True

def get_ranges(num_list):
    out_list = [] # create and define additional list
    out_list.append([])
    j = 0
    for i in range(0, len(num_list) - 1):
        out_list[j].append(num_list[i]) # in any case we append the element
        if num_list[i] + 1 != num_list[i + 1]: # check if we should go to the next range
            j += 1
            out_list.append([])
    out_list[j].append(num_list[len(num_list) - 1])
# I just wanted to show off with the comprehension
    out_list = ["-".join([str(out_list[j][0]), str(out_list[j][-1])]) if len(out_list[j]) != 1 else str(out_list[j][0]) for j in range(0, len(out_list))]

    return '"{}"'. format(', '.join(out_list))



#tests
print(check_str('The VeRy quick Brown Fox 23132,,,,') )

print(is_prime(45345),is_prime(45346),is_prime(4),is_prime(2),is_prime(1),is_prime(3),is_prime(0),is_prime(-5))

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]),get_ranges([4,7,10]),get_ranges([2, 3, 8, 9]))