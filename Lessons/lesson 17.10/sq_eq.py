import math

a = 3
b = -14
c = -5

D = b*b - 4*a*c

print(D)

D/0

x_1 = (-b + math.sqrt(D)) / (2*a)
x_2 = (-b - math.sqrt(D)) / (2*a)

print(x_1, x_2)