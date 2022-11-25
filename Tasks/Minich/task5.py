def check_str(s):
    l=0
    u=0
    for i in s:
        if i.islower():
            l+=1
        else:
            u+=1
    print(str(u) + ' upper case,' + str(l) + ' lower case')

def is_prime(n):
    k=0
    for i in range(2,n):
        if n%i==0:
            k+=1
            break
    print(f'{not bool(k)}')

def get_ranges(s):
    d=[]
    k1 = s[0]
    k2 = s[0]
    for i in range(1,len(s)):
        if k2+1 == s[i] and i!=len(s)-1:
            k2+=1
            continue
        else:
            if k1!=k2:
                d.append(str(k1)+'-'+str(k2))
            else:
                d.append(k1)
            if i ==len(s)-1:
                d.append(s[i])
            k1=s[i]
            k2=k1
    print(d,sep=',')


#1
str1 = input("Please enter string\n")
check_str(str1)

#2
n = input("Please enter digit\n")
is_prime(int(n))

#3
get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4,7,10]) 
get_ranges([2, 3, 8, 9])