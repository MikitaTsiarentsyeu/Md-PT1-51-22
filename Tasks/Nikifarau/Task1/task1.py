import math
from decimal import Decimal

amount_of_deposit = Decimal(input("Enter your deposit amount:\n"))
period = int(input("For how many years is the deposit:\n"))
rate = Decimal(input("What percentage do you prefer:\n"))
is_deposite_capitalization = int(input("select the monthly capitalization, press 1 yes or 2 no:\n"))

count_of_days = period*365
                              # bank settlements in days

if is_deposite_capitalization == 2:
    sum_mounth = round((amount_of_deposit*rate*count_of_days/365) / 100,2)
    sum_amount = amount_of_deposit + sum_mounth

                             # the amount deposited plus the accumulated interest
    print(f"Congratulations Your total amount {sum_amount}")
elif is_deposite_capitalization == 1:
    sum_amount_c = round(amount_of_deposit*((1+rate/12/100)**(12*period)),2) 
    print(f"Congratulations Your total amount {sum_amount_c}") 
else:
    print("Error Check the capitalization data")