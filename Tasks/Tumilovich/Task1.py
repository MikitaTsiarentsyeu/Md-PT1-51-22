from decimal import *
Dep = Decimal(input("What's your deposit? \n"))
Yrs = Decimal(input('How many years? \n' ))
Int = Decimal(input('Annual interest in % \n'))
Cap = input('You want to add monthly capitalization? \n yes / no \n')
if Cap == 'yes':
    _SUM2 = Dep * (1 + Int / 100 / 12) ** (Yrs * 12)
    print(_SUM2)
    if _SUM2 >= 1000000:
        print("You're gonna be a millionaire!")
elif Cap == 'no':
    _SUM1 = Dep * (1 + Int / 100) ** Yrs
    print(_SUM1)
    if _SUM1 >= 1000000:
        print("You're gonna be a millionaire!")


# не понял как и где я могу применить getcontext().prec = 2,
# чтобы он выводил, скажем, 2 знака после запятой

