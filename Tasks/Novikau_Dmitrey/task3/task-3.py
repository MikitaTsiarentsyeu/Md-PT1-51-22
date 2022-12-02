d = {'one' : 1, 'two' : 2, 'three' : 3, 'four': 4, 'five' : 5,
    'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9, 'ten' :10,
    'eleven' : 11, 'twelve' : 12, 'thirteen' : 13, 'fourteen' : 14,
    'fifteen' : 15, 'sixteen' : 16, 'seventeen' : 17, 'eighteen' : 18, 'nineteen': 19, 'twenty': 20}

number = input("six eleven seven two one five thirteen twenty\n")
#number="six eleven seven two one five thirteen twenty"
number = number.split(' ')

arr=[]

for i in number:
    if i in d:
        arr.append(d[i])
    else:
        print("nothing")
print('array converted to a number:\n',arr)
arr = list(set(arr)) 
arr.sort()
print("the array is sorted and without repetitions\n",arr)

count=0
brr = []
while(count+1<len(arr)):
    if(count%2==0):
        brr.append(arr[count]+arr[count+1])
    else:
        brr.append(arr[count]*arr[count+1])
    count+=1
print("array of sum and multiplications\n", brr)
sum=0

for i in arr:
    if(i%2!=0):
        sum+=i

print('total sum of all odd elements\n',sum)        