# Task 1. Calculation of income from the deposit.
from decimal import Decimal as dec

deposit = dec(input('Enter the deposit amount please\n'))
percent = dec(input('Enter percentage per annum please\n'))
term_year = int(input('Enter number of years please\n'))
term_month = term_year*12                                      # months used in calculations

if input('Whether to take into account the capitalization of savings per month? (y/n)\n').lower() == 'y':
    cash = deposit * ((percent / 1200 + 1) ** term_month)
    cash = round(cash, 2)
else:
    cash = deposit * (percent * term_month / 1200 + 1)
    cash = round(cash, 2)


print(f'Your final sum will be {cash},\nprofit is {cash - deposit}\n')
input('Press anything to quit')                                # to keep console open for a while

