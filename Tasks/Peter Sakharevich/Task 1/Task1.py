import math
deposite = int(input('Введите сумму депозита:\n'))
deposite_term = int(input('Введите срок депозита, лет:\n'))
percentage = float(input('Введите процентную ставку:\n'))
capitalization = input('Наличие ежемесячной капитализации(y/n):\n')
if capitalization == 'n':
    total_amount = round(deposite * math.pow((1 + percentage / 100 ), deposite_term), 2) # годовая капитализация
    print(total_amount)
elif capitalization == 'y':
    total_amount = round(deposite * math.pow((1 + percentage / (100 * 12) ), deposite_term * 12), 2) # ежемесечная капитализация
    print(total_amount)
else: print('Неправильно введено значение капитализации') 
