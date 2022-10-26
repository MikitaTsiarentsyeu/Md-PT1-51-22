import decimal

a = decimal.Decimal(input("Начальная сумма:\n"))
b = decimal.Decimal(input("Срок в годах:\n"))
c = decimal.Decimal(input("Годовой процент:\n"))
d = input("Ежемесячная капитализация (введите ДА или НЕТ):\n")

x = a*(1+(c/(100*12)))**(12*b)

y = a*(1+(c/100))**b

if d == "ДА":
    print("Итоговая сумма на счету: ", x)

elif d == "НЕТ":
    print("Итоговая сумма на счету: ", y)