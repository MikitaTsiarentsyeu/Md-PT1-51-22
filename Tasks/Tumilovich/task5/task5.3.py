
def get_ranges(l):
    l = list(map(str, l))        # string type is more convinient later
    new_l = [str(l[0])]
    str1 =''                     # str1 type is string
    for i in range(1, len(l)):                # starting with index 1 to compare current with element before
        if int(l[i]) == int(l[i-1]) + 1:
            new_l.append(str(l[i]))
            if l[i] == l[-1]:                         # if it is the last index and numbers are included in range(not separate) we need to write this data
                str1 += new_l[0] + '-' + new_l[-1]
        else:
            if len(new_l) > 1:
                str1 += str(new_l[0]) + '-' + str(new_l[-1])
            elif len(new_l) == 1:
                str1 += str(new_l[0])
            if l[i] != l[-1]:                           # if it is not the last index, we need separator ','
                        str1 += ','
            else:                                       # if it is the last index we need to add data in string
                str1 +=',' + l[i]
            new_l = [str(l[i])]
    return print(str1)

get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4,7,10])
get_ranges([2, 3, 8, 9])
