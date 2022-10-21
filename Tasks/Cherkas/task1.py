
money, term, per = float(input('Enter money: \n')), float(input('Enter term: \n')), float(input('Enter percent : \n'))
c = input('capitalization once a month or once a year?(M/Y):\n')
if c == 'Y':
    sum_1 = money*((1+(per/100)))**term
    print(sum_1)
elif c == 'M':
    sum_2 = money * (1 + ((per / 100)/12)) ** (term*12)
    print(sum_2)
else:
    Print('Capitalization is not defined. Try again')
