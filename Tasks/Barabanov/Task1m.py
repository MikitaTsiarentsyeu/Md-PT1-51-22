from decimal import *
print("Hello. This is a compound interest calculator.\nSpecify the amount, period(s) and interest rate:")

while True:
    p, t, r = Decimal(input("Enter deposit amount:\n")), Decimal(input("Enter deposit period(s):\n")), Decimal(input("Enter deposit interest rate:\n")),
    try:
        if p <=0 or t <=0 or r <=0:
            raise Exception
        Decimal(p),Decimal(t),Decimal(r)
        break
    except Exception:
        print("Error,Meaning cannot be negative!")

while True:
    per = input("Use month capitalisation? Write 'Yes' or 'No'\n")
    try:
        if per.lower() == "yes":
            n = Decimal(1)
        elif per.lower() == "no":
            n = Decimal(12)
        else:
            raise Exception
        break
    except Exception:
        print("Incorrect value!")

percent = (p * ((1 + r/100/n)**(n*t)))

print("Initial deposit amount:\t", p)
print("Deposit period, years:\t", t)
print("Deposit rate, %:\t\t", r)
print("Month capitalisation:\t", per.title())
print("Final deposit amount:\t", percent.quantize(Decimal("1.00"),ROUND_FLOOR))
print("Profit: \t\t\t\t", (percent.quantize(Decimal("1.00"),ROUND_FLOOR))- p)