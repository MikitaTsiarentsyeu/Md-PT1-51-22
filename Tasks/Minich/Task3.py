digitsdic = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20}

#strenter = input("Please enter digits\n")

#for example, a ready string for testing

strenter = 'six seven five eight three two one thirteen eighteen seven five'
lis = strenter.split()
lis2 = []
lis3 = []
lis4 = []
sum=0
k=0
for i in lis:
    x = digitsdic[i]
    lis2.append(x)
    k+=1
    if k%2==0:
        lis4.append(x*lis2[k-2])
    elif k>2:
        lis4.append(x+lis2[k-2])
    if x%2!=0:
        sum=sum+x
    if x not in lis3:
       lis3.append(x)

print(*lis2,sep=' ')
print(*lis3,sep = ' ')
print(*sorted(lis2),sep=' ')
print(*lis4,sep = ' ')
print(sum)