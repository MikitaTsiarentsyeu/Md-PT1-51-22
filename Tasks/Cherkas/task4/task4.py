while True:
    answer = input('Enter the line lenght (lenght>35):\n')
    if answer.isdigit() and int(answer)>35:
        break
    continue

with open('text.txt', 'r', encoding='utf-8') as f:
    with open('text_result.txt', 'w', encoding='utf-8') as f2:
        file = f.read()
        index = 0
        counter = 0
        
        while index<=len(file):
            string = file[index:int(answer)+index]
            if '\n' in string:
                string = file[index:file.find("\n", index)]
                
                counter=index+int(answer)-file.find("\n",index)
                
            else:
                while string[-1] not in [' ', ',', '.']:
                    string = string[:-1]
                    counter+=1
                if len(string) != len(string.lstrip()):
                    counter+=1
                    string=string.lstrip()
                if len(string) != len(string.rstrip()):
                    counter+=1
                    string=string.rstrip()

                while len(string) < int(answer):
                    string = string.replace(' ', '  ', int(answer) - len(string))
            
            index=index-counter+1+int(answer)
            counter=0
            f2.write(string + '\n')
        print('file is saved ')
    

