def check_str(value):
    l = 0
    u= 0
    for i in value:
        if i.islower():
            l = l+1
        elif i.isupper():
            u=u+1
        else:
            pass
    print(f"{u} upper case, {l} lower case ")

check_str("Hello Mikita")


def is_prime(num):
    if num in [1,2,3,5,7]:
        return True
    elif num%2 == 0 or num%2 == 0 or num%3 == 0 or num%7 == 0: 
        return False
    else:
        return True

print(is_prime(1020))
print(is_prime(1019))

def get_ranges(list_num):
    try:
       
        mass1 = []
        mass2 = [[],[],[],[],[],[],[],[],[],[],]

        for i in range(len(list_num)-1):
            if list_num[i+1] - list_num[i] ==1:
                mass1.append(list_num[i])
                mass1.append(list_num[i+1])
            else:
                continue
            
        sorted_li = sorted(list(set(mass1)))
        single_nums = list(set(list_num) - set(sorted_li ))

        k=0
        for i in range(len(sorted_li)-1):
            if sorted_li[i+1] - sorted_li[i] ==1:
                mass2[k].append(sorted_li[i])
                mass2[k].append(sorted_li[i+1]) 
                mass2[k] = sorted(list(set(mass2[k])))
            else:
                k+=1

        z = k+1
            
        for i in single_nums:
            mass2[z].append(i)
            z+=1

        sorted_mass2 = sorted(mass2)
        sorted_mass2 = list(filter(None, sorted_mass2))

        for i in sorted_mass2:  
            if len(i)>2:
                del i[1:len(i)-1]
            
        str2 = ''
        for i in sorted_mass2:
            i = str(i)+'|'
            str2 +=i

        str2 = str2.replace('[', '').replace(']', '').replace(',', '-').replace(' ', '').replace('|',',')
        for i in range(len(str2)-1):
            if (str2[i] == ',') and (str2[i+1] != ' '):
                str2 = str2[:i+1] + ' ' + str2[i+1:]

        final_str2 = ''
        for i in range(len(str2)-1):
            final_str2+= str2[i]
        print(final_str2)

    except IndexError:
        print("List is too long! Insert less numbers!")
        
# i know that 3rd task is not ideal and simple in code, but i did my best with current knowledge :)

get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  
get_ranges([4,7,10])  
get_ranges([2, 3, 8, 9])  
