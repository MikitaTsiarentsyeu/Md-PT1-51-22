while True:
    n = input('Input number of symbols > 35 in a row:\n')
    if not n.isdigit():
        print('error: input must be digit')
        continue
    if int(n) <= 35:
        print('error: number must be >35 \nTry again \n')
        continue
    n = int(n)
    break


with open('text.txt', 'r') as donor:
    with open ('test4.txt', 'w') as recepient:

        for line in donor:
            start = 0
            while line:
                count = 0
                line = line[start:]
                if len(line) > n:
                    s = line[:n]
                    nexts = line[n]
                    for i in range(len(s)):
                        if s[i] in ('’', '“', '”'):
                            start += 2

                    for i in range(len(s)):
                        if s[-1] != ' ':
                            if nexts != ' ':
                                count += 1
                                s = s[:-1]
                            else:
                                break
                        else:
                            break

                    start = n - count
                    count += len(s) - len(s.strip())
                    s = s.strip()
                    counts = s.count(' ')
                    m = count // counts

                    if m == 0 or m == 1:
                        s = s.replace(' ', '  ', count)
                        count = count - counts
                        if count > 0:
                            s = s.replace('  ', '   ', count)
                    else:
                        s = s.replace(' ', ' ' * (m + 1), count)
                        count -= m * counts
                        s = s.replace(' ' * (m + 1), ' ' * (m + 2), count)
                    recepient.write(s + '\n')


                else:
                    recepient.write(line.lstrip())
print(f'test4.txt with {n} symbols in a row IS CREATED')
