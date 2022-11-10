import math
capitalization = input("Include monthly capitalization (enter yes/no):\n")

o = float(input("Enter your budget:\n"))
p = float(input("Enter percent:\n"))
n = float(input("Enter term (year):\n"))

F = int(o*(1+(p*1/100)/12)**(n*12))
S = int(o*(1+n*1/100*p))

if capitalization == ("yes"):
    print("Your amount for" , n , "years:\n" , F)
elif capitalization == ("no"):
    print("Your amount for" , n , "years:\n" , S)
else:
    print("SORRY!")


