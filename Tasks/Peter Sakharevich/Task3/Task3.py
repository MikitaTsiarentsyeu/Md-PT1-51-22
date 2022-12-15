numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,
"nine":9, "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15,
"sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19, "twenty":20}
line_numbers = input('Enter line of numbers between one and twenty: \n')
l=[]
for i in line_numbers.split(" "):
    l.append(numbers[i])
print(l)
print(list(set(l)))
print(sorted(l))
#print(sorted(list(set(l)))) from 1 to 3
i = 0
while i < len(l) - 1:
    if i == 0 or i % 2 == 0:
        print(l[i] * l[(i + 1)], end=" ")
    else:
        print(l[i] + l[(i+1)], end=" ")
    i+=1
print(" ")
sum_odd_number = 0
for i in range(len(l)):
    if l[i] % 2 != 0:
        sum_odd_number += l[i]
print(sum_odd_number)