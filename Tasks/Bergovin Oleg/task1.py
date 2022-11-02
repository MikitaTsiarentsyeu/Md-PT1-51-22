import math
from decimal import Decimal
a = Decimal(int(input('Sum of money')))
b = Decimal(int(input('Amount of percents')))
c = Decimal(int(input('Amount of years')))
d_1 = a*(b/100)
D_1 = a + d_1
d_2 = D_1*(b/100)
D_2 = D_1 + d_2
d_3 = D_2*(b/100)
D_3 = D_2 + d_3
d_4 = D_3*(b/100)
D_4 = D_3 + d_4
d_5 = D_4*(b/100)
D_5 = D_4 + d_5
print ('current money left', D_5)