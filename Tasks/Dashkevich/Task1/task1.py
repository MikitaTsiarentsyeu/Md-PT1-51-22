from decimal import *

def capitalization_monthly ():
    month_amount_total = Decimal.from_float(start_capital *
    (1 + ((annual_interest_rate / 100) / 12)) ** (12 * year_term))
    return month_amount_total.quantize(Decimal("1.00"), ROUND_HALF_UP)

print("You can calculate amount in the account at the end of the specified period in this program\n")

start_capital = int(input("Sum of deposit: \t"))
year_term = int(input("Term (years): \t"))
annual_interest_rate = int(input("Percent: \t"))

print("Do you want to enable monthly capitalization?")
user_choice = input("Write Y(Yes) for monthly capitalization or N(No) for other value for different type of capitalization:\n")

if user_choice == "Y" or user_choice == "y":
   print("Total sum is", capitalization_monthly())
elif user_choice == "N" or user_choice == "n":
    capitalization = int(input("Capitalization: \t"))
    final_ammount = Decimal.from_float(start_capital *
    (1 + ((annual_interest_rate / 100) / capitalization)) ** ( capitalization * year_term))
    print("Total sum is", final_ammount.quantize(Decimal("1.00"), ROUND_HALF_UP))
