def get_ranges(list):
    l = [] 
    for i in range(len(list)-1):
        if list[i+1] == list[i]+1 and list[i-1] != list[i]-1:
            l.append(str(list[i]))
            l.append('-')
        elif list[i+1] != list[i]+1 and list[i-1] == list[i]-1:
            l.append(str(list[i]))
            l.append(',')
        elif list[i+1] != list[i]+1 and list[i-1] != list[i]-1:
            l.append(str(list[i]))
            l.append(',')
    l.append(str(list[-1]))
    return ''.join((l))

       
   

list = [0, 2, 3, 4, 7, 8, 10, 12]
x = get_ranges(list)
print(repr(x))