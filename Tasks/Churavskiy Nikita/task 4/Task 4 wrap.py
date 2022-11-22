from textwrap import wrap

while True:
    enter_number = input('please, enter your text number:\n')
    if enter_number.isdigit() == False:
        print('not correctly value, repeat your enter, string can be only number')
    elif (int(enter_number)) <= 35:
        print('not correctly value, repeat your enter, max width=35')
    else:
        width=int(enter_number)
        break
    
with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

def res_width(line, width):
    gap_width, max_replace = divmod(width - len(line) + line.count(' '), line.count(' '))
    return line.replace(' ', ' ' * gap_width).replace(' ' * gap_width, ' ' * (gap_width + 1), max_replace)

def lines_formatter(text, width):
    lines = wrap(text, width, break_long_words=False)
    for i, line in enumerate(lines[:-1]):
        if len(line) <= width and line.count(' '):
            lines[i] = res_width(line, width).rstrip()
    res = '\n'.join(lines)
    with open('new_text.txt', 'w+', encoding='utf-8') as f1:
        f1.write(res)
    return f'you can open and read file in: new_text.txt'


print(lines_formatter(text, width))