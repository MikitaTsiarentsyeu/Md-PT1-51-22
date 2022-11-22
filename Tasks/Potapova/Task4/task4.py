# Even if the string length minimum is 35 it is possible to get string length less than that limit.
# Words, that reach the limit, will be cut forcibly. Strings with \n are not filled with extra spaces.


while True:
    limit = int(input('Please enter the string size in whole numbers.\nIt must be greater than 35 or equal to.\n'))
    if limit < 35:
        print(f'Incorrect input. {limit} < 35')
        continue
    break

with open("text.txt", "r", encoding="utf8") as rf:
    with open("new_text.txt", "w", encoding="utf8") as wf:
        for line in rf:
            while line:
                if len(line) > limit:
                    s_line = line[:limit + 1].lstrip()
                    if ' ' in s_line:
                        s_line = s_line[:(s_line.rfind('\n' if '\n' in s_line else ' ') + 1)].split()
                        i, pos = 1, 1
                        while len(''.join(s_line)) < limit:
                            s_line.insert(pos, ' ')
                            i = i + 1 if (pos + i + 1) >= len(s_line) else i
                            pos = pos + i + 1 if (pos + i + 1) < len(s_line) else i
                        wf.write(''.join(s_line) + '\n')
                        line = line[line[:limit + 1].rfind('\n' if '\n' in line[:limit + 1] else ' ') + 1:]
                    else:
                        wf.write((line[:limit].strip()) + '\n')
                        line = line[limit:]
                else:
                    wf.write((line.strip()) + '\n')
                    line = ''


print('File with formatted text "new_text.txt" is ready')


