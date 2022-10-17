import math
a, b, c = float(input("Enter a:\n")), float(input("Enter b:\n")), float(input("Enter c:\n"))

D = b*b - 4*a*c

print(D)

if D > 0:
    x_1 = (-b + math.sqrt(D)) / (2*a)
    x_2 = (-b - math.sqrt(D)) / (2*a)
    print(x_1, x_2)
elif D == 0:
    print(-b/(2*a))
else:
    print("there are no roots")