import decimal

# inputs
sum_of_money = decimal.Decimal(input("Welcome! How much money do you want to deposit?\n"))
period = decimal.Decimal(input("How many years do you want to keep it?\n"))
interest_rate = decimal.Decimal(input("What rate are you interested in (in %)?\n"))

# Take value as string, will check later
capitalization = input("Do you want monthly compounding (yes or no)?\n")

# Set capitalization to true by default
capitalised = True

# If the customer doesn't agree explicitly, no monthly compounding for him, just annual
if capitalization.lower() not in ['yes','y','yeah']:
    capitalised = False

result = decimal.Decimal(0)

if capitalised: # monthly compounding
    result = decimal.Decimal(sum_of_money * (1 + interest_rate/(12 * 100)) ** (period * 12))
else: # annual compounding
    result = decimal.Decimal(sum_of_money * (1 + interest_rate / (100)) ** (period))

print("You will get ", round(result, 2))