o = input("Enter your number (>35)\n")
with open("/Lessons IT/Md-PT1-51-22/Tasks/Novikau_Dmitrey/task4/text.txt", 'r') as t:
    add = t.read()
    #print(add)
    i = 1
    add=add.replace("\n", " ")
    outStr=add[0]
    print(len(add))
    while(i < len(add)):
        if (i % int(o) == 0):
            if (add[i] != " "):
                j=i-1
                tempStr=""
                while(add[j] != " "):
                    tempStr+=add[j]
                    j-=1    
                outStr= outStr[:-(i-j)]
                outStr+="\n"
                outStr+= ''.join(reversed(tempStr))
            else:
                i+=1
                outStr+="\n"

        outStr+=add[i]
        i += 1
print(outStr)
