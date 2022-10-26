from decimal import Decimal
import math


depSum = Decimal(input("Please input deposit amount:\n"))
depPer = Decimal(input("Please input annual percentage:\n"))
depTerm = Decimal(input("Please input deposit term in years:\n"))
monCap = input("Do you want to apply monthly capitalization? y/n\n")

if monCap == "y":
    total = depSum*pow(1+depPer/100/12, (depTerm*12))
else:
    total = depSum + depSum*depPer/100*depTerm

print("Totally you will get: ", Decimal(total).quantize(Decimal("1.0000")))