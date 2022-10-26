import math
capitalization = input("Include monthly capitalization (enter yes/no):\n")
o = float(input("Enter start-up money:\n"))
p = float(input("Enter percent:\n"))
n = int(input("Enter term (in years):\n"))


F = int(o*(1+n*p/100))
S = int(o*(1+p/100/12)**(n*12))

if capitalization == "yes":
    print("Your amount for" , n , "years:\n" , S)
elif capitalization == "no":
    print("Your amount for" , n , "years:\n" , F)
else:
    print("Sorry!")
