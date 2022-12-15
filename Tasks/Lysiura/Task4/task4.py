while True:
    line_length = input('Enter num > 35: ')
    if not line_length.isdigit():
        print('You have to enter num > 35.')
        continue
    line_length = int(line_length)
    if line_length <= 35:
        print('You have to enter num > 35')
        continue
    break      
with open('text.txt', 'r', encoding = 'utf-8') as f:
  with open('edited_text.txt', 'w', encoding = 'utf-8') as ed_f:
        text = f.read().split() 
        line = [] 
        for word in text:
            if line_length - len(''.join(line)) >= len(word): 
                line.append(word)
                line.append(' ') 
                
            else:
                line.pop() 
                while len(''.join(line).rstrip()) != line_length: 
                    for i in range(len(line)):
                        if len(''.join(line).rstrip()) == line_length: 
                            break
                        if line[i] != ' ':
                            line.insert(i + 1, ' ')
                ed_f.write(''.join(line)+ '\n')
                line = [word, ' ']               
print('Edited text is ready ')
