while True:
    enter_number = input('please, enter your text number:\n')
    if enter_number.isdigit() == False:
        print('not correctly value, repeat your enter, string can be only number')
    elif (int(enter_number)) <= 35:
        print('not correctly value, repeat your enter, max width=35')
    else:
        width=int(enter_number)
        break
    
def sorting_text():
    with open('text.txt', 'r', encoding='utf-8') as text:
        with open('new_text.txt', 'w+') as f1:
            for value in text:
                while value:
                    if len(value) > int(enter_number):
                        content = value[:int(enter_number) + 1].lstrip()
                        if ' ' in content:
                            content = content[:(content.rfind('\n' if '\n' in content else ' ') + 1)].split()
                            some, some2 = 1, 1
                            while len(''.join(content)) < int(enter_number):
                                content.insert(some2, ' ')
                                some = some + 1 if (some2 + some + 1) >= len(content) else some
                                some2 = some2 + some + 1 if (some2 + some + 1) < len(content) else some
                            f1.write(''.join(content).replace("’","").replace("“","").replace("”","") + '\n')
                            value = value[value[:int(enter_number) + 1].rfind('\n' if '\n' in value[:int(enter_number) + 1] else ' ') + 1:]
                        else:
                            f1.write(value[:int(enter_number)].replace("’","").replace("“","").replace("”","").strip() + '\n')
                            value = value[int(enter_number):]
                    else:
                        f1.write((value.replace("’","").replace("“","").replace("”","").strip()) + '\n')
                        value = ''
    return f'you can open and read file in: new_text.txt'

print(sorting_text())