# Task 1. Calculation of income from the deposit.
from decimal import Decimal as dec

deposit = dec(input('Enter the deposit amount please\n'))
percent = dec(input('Enter percentage per annum please\n'))
term_year = int(input('Enter number of years please\n'))
term_month = term_year*12                                      # months used in calculations
capit = ''

while capit != 'y' and capit != 'n':
    capit = input('Whether to take into account the capitalization of savings?\n (y/n)\n').lower()
    if capit.lower() == 'y':
        capit_term = ''
        while capit_term != 'y' and capit_term != 'm':
            capit_term = input('Should capitalization be per year or per month?\n (y/m)\n').lower()
            if capit_term.lower() == 'm':
                cash = deposit * ((percent / 1200 + 1) ** term_month)
                cash = round(cash, 2)
            elif capit_term.lower() == 'y':
                cash = deposit * ((percent / 100 + 1) ** term_year)
                cash = round(cash, 2)
            else:
                print('Please, make a choice!')
    elif capit.lower() == 'n':
        cash = deposit * (percent * term_month / 1200 + 1)
        cash = round(cash, 2)
    else:
        print ('Please, make a choice!')


print(f'Your final sum will be {cash},\nprofit is {cash - deposit}\n')
input('Press anything to quit')                                # to keep console open for a while

