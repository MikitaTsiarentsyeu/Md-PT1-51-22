[3,2,4,6,5,8,7,9,1,10]

4, 2
[3,2,5,6,4,8,7,9,1,10]

5, 6
[3,2,5,6,4,7,8,9,1,10]

import random

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def generate_index(n):
    return random.randint(0, n-1)

def swap(l):
    i = generate_index(len(l))
    j = i
    while i == j:
        j = generate_index(len(l))
    l[i], l[j] = l[j], l[i]

def sort(l):
    counter = 0
    while not is_sorted(l):
        swap(l)
        counter += 1
        print(counter)


l = [3,2,4,6,5,8,1,7,9]
sort(l)

