
# Task 01
## Bank deposit calculation:
For bank deposit calculation:
1. Ask User to input deposit amount, term in years and annual percentage. 
2. Ask User to enable or disable monthly capitalization.
3. Count and display the total. 
## Solution:

```python
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
```