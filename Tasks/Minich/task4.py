#Description: We analyze in parts. If the next character is a space, add it to the list. 
# Otherwise, we look for the first space from the end of the string. 
# Found, we transfer the word to the next part, and fill in the lack with spaces. 
# At the end, we fill the file with a list through line breaks

str1 = input("Please enter string\n")

len1 = len(str1)+1
len2 = len(str1)

print('Your length: ' + str(len2))

s = []
k=0
with open("text.txt","r") as f:
    part = f.read(len1)
    while part:
        part = part.replace('\n',' ')
        if part[len(part)-1]==' ':
            s.append(part[0:len2])
            part = f.read(len1)
        else:
            linelen = len(part)-1
            while linelen!=0:
                if part[linelen-1]==' ' or linelen<len1:
                    if linelen!=len(part)-1:
                        s.append(part[0:linelen]+(k*" "))
                        k+=1
                    else:
                        s.append(part[0:linelen])
                        k+=1
                    break
                else:
                    linelen-=1
                    k+=1
            f.seek(f.tell()-k)
            k=0
            part = f.read(len1)
            size = len(s)
            

with open("text.txt","w") as f:
    for i in s:
        f.write(i + '\n')

f.close()
print('Сompleted successfully')