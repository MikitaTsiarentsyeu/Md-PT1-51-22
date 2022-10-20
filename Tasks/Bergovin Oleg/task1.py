import math
from decimal import Decimal
a = Decimal('20000')
b = Decimal('0.15')
c = Decimal('5')
d_1 = a*b
D_1 = a + d_1
d_2 = D_1*b
D_2 = D_1 + d_2
d_3 = D_2*b
D_3 = D_2 + d_3
d_4 = D_3*b
D_4 = D_3 + d_4
d_5 = D_4*b
D_5 = D_4 + d_5
print ('current money left', D_5)