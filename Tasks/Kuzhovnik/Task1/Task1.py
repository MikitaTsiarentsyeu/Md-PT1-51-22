import math
from decimal import *

while True:
    p = input("Enter deposit amount:\n")
    try:
        if Decimal(p) <= 0:
            raise Exception
        Decimal(p)
        break
    except Exception:
        print("Incorrect value!")
p = Decimal(p)

while True:
    t = input("Enter deposit period, years:\n")
    try:
        if Decimal(t) <= 0:
            raise Exception
        Decimal(t)
        break
    except Exception:
        print("Incorrect value!")
t = Decimal(t)

while True:
    r = input("Enter deposit rate, pct.:\n")
    try:
        if Decimal(r) <= 0:
            raise Exception
        Decimal(r)
        break
    except Exception:
        print("Incorrect value!")
r = Decimal(r)

while True:
    cap = str(input("Use month capitalisation? Write 'Yes' or 'No'\n"))
    try:
        if cap.lower() == "yes":
            n = Decimal(12)
        elif cap.lower() == "no":
            n = Decimal(1)
        else:
            raise Exception
        break
    except Exception:
        print("Incorrect value!")

p_total = (p * ((1 + r/100/n) ** (n * t))).quantize(Decimal("1.00"), ROUND_FLOOR)
print("Initial deposit amount:\t", p)
print("Deposit period, years:\t", t)
print("Deposit rate, %:\t\t", r)
print("Month capitalisation:\t", cap.title())
print("Final deposit amount:\t", p_total)
print("Profit: \t\t\t\t", p_total - p)

while True:
    det_ans = str(input("Show details? Write 'Yes' or 'No'\n"))
    try:
        if det_ans.lower() == "yes":
            True
        elif det_ans.lower() == "no":
            exit("Ok!")
        else:
            raise Exception
        break
    except Exception:
        print("Incorrect value!")

total_periods = int(t * n)
curr_period = 1
pp = p
print("Period\tStart balance\t\tProfit\t\t\tResult")
while total_periods >= curr_period:
    p = pp
    pp = p * (1 + r / 100 / n)
    start_bal =  str(p.quantize(Decimal("1.00"), ROUND_FLOOR))
    profit = str(pp.quantize(Decimal("1.00"), ROUND_FLOOR) - p.quantize(Decimal("1.00"), ROUND_FLOOR))
    result = str(pp.quantize(Decimal("1.00"), ROUND_FLOOR))
    print(str(curr_period) + "\t\t" + start_bal + "\t\t\t" + profit + "\t\t\t" + result)
    curr_period = curr_period + 1