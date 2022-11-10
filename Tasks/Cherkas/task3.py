d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
'nine':9,'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16,
'seventeen':17, 'eighteen':18, 'nineteen':19,'twenty':20}

string = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
lst = string.split()
lst_1 = []
for i in lst:
    lst_1.append(d[i])
print(lst_1)
lst_1 = sorted(list(set(lst_1)))
print(lst_1)
for i in range(len(lst_1)-1):
    print(lst_1[i]+lst_1[i+1] if i%2==0 else lst_1[i]*lst_1[i+1],end=' ')

sum = 0
for i in lst_1:
    if i%2==1:
        sum+=i
print(f'\nsum = {sum}')