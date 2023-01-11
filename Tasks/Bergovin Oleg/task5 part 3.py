
def get_ranges(l):
    l = list(map(str, l))        
    new_l = [str(l[0])]
    str1 =''                     
    for i in range(1, len(l)):                
        if int(l[i]) == int(l[i-1]) + 1:
            new_l.append(str(l[i]))
            if l[i] == l[-1]:                         
                str1 += new_l[0] + '-' + new_l[-1]
        else:
            if len(new_l) > 1:
                str1 += str(new_l[0]) + '-' + str(new_l[-1])
            elif len(new_l) == 1:
                str1 += str(new_l[0])
            if l[i] != l[-1]:                          
                        str1 += ','
            else:                                       
                str1 +=',' + l[i]
            new_l = [str(l[i])]
    return print(str1)

get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4,7,10])
get_ranges([2, 3, 8, 9])
