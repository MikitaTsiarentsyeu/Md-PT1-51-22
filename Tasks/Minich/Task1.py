a = float(input('Enter initial amount\n'))
b = int(input('Enter deposit term in years\n'))
c = float(input('Enter deposit rate\n'))

d = input("Enable monthly capitalization? Y(yes)/N(no)\n")

if (d=='y') or (d=='Y'):    
    S = round(a * (1+c/100)**b,2)
else:
    S = round(a * (1+c/100*b),2) 

print('Total amount: ' + str(S))