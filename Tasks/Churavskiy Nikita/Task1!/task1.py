from decimal import Decimal

sum = Decimal(input('enter your sum \n'))
date = Decimal(input('enter period in years \n'))
percent = Decimal(input('enter your percent \n'))  
capitalize = str(input('do you want capitalize every month or one time in year?,\nanswer 1 or 2\n'))

if capitalize==str(1):
    s = int(round(sum*(1+(percent/100/12))**date*12)+sum)
    print(f'your deposit result\n{s}')
else:
    s1 = int(round(sum*percent*date*365/365)/100)+sum
    print(f'your deposit result\n{s1}')



