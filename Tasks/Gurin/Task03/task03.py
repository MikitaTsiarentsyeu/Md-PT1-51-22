d = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20
}

str = input("Please enter a string containing numbers separated by a space, all numbers must be greater than 0 and less than 21 \n")
l = []
for i in str.split():
    l.append(d[i])

l = sorted(list(set(l)))

print("Your sort ascending list without duplicates in number view is:",l,"\n")

for i in range(len(l)-1):
    if i%2 == 0:
        print("multiplication of the [",i+1,"] and [",i+2,"] numbers is: ", l[i]*l[i+1],"\n")
    else:
        print("sum of the [",i+1,"] and [",i+2,"] numbers is: ", l[i]+l[i+1],"\n")


sum = 0
for i in l:
    if i%2 != 0:
        sum += i
print("sum of all odd numbers:\n", sum)        