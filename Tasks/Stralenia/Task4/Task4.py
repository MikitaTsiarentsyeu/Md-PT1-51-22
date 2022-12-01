      
with open("text.txt", "r", encoding="utf8") as f:
    
    length = int(input('Enter the string size more than 35:\n'))
    if length < 35:
        print('Incorrect size')    
           
    with open("correct_text.txt", "w", encoding="utf8") as w:
        
        for line in f:
            
            while line:
                
                if len(line) > length:
                    new_line = line[:length + 1]
                    
                    if ' ' in new_line:
                        new_line = new_line[:(new_line.rfind('\n' if '\n' in new_line else ' ') + 1)].split()
                        
                        num = 1
                        space = 1   
                        while len(''.join(new_line)) < length:
                            new_line.insert(num, ' ')
                            if (num + space + 1) >= len(new_line):
                                space = space + 1
                                num = 1 
                            else:
                                num = num + space + 1
                        
                        w.write(''.join(new_line) + '\n')
                        line = line[line[:length + 1].rfind('\n' if '\n' in line[:length + 1] else ' ') + 1:]                      
                                   
                else:
                    w.write((line.strip()) + '\n')
                    line = ''
