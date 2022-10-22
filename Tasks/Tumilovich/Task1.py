from decimal import *
Dep = Decimal(input("What's your deposit? \n"))
Yrs = Decimal(input('How many years? \n'))
Int = Decimal(input('Annual interest in % \n'))
Cap = input('You want to add monthly capitalization? \n yes / no \n')

if Cap == 'yes':
    _SUM2 = Dep * (1 + Int / Decimal('100') / Decimal('12')) ** (Yrs * Decimal('12'))   # Перестраховался и перед всеми цифрами поставил Decimal и ''. может есть проще способ?
    getcontext().prec = len(str(int(_SUM2))) + 2                                        # для вывода пользователю решил ограничить вывод до 2х знаков после запятой
    _SUM2 *= 1                                                                          # чтобы prec применился
    print(_SUM2)
    if _SUM2 >= 1000000:
        print("You're gonna be a millionaire!")
elif Cap == 'no':
    _SUM1 = (Dep * (1 + Int / Decimal('100')) ** Yrs)
    getcontext().prec = len(str(int(_SUM1))) + 2
    _SUM1 *= 1
    print(_SUM1)
    if _SUM1 >= 1000000:
        print("You're gonna be a millionaire!")


