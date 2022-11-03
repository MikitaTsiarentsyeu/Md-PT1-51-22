import datetime

d = {
    0: ['ноль', 'первого'],
    1: ['один', 'первого'],
    2: ['два', 'второго'],
    3: ['три', 'третьего'],
    4: ['четыре', 'четвертого'],
    5: ['пять', 'пятого'],
    6: ['шесть', 'шестого'],
    7: ['семь', 'седьмого'],
    8: ['восемь', 'восьмого'],
    9: ['девять', 'девятого'],
    10: ['десять', 'десятого'],
    11: ['одиннадцать', 'одиннадцатого'],
    12: ['двенадцать', 'двенадцатого'],
    13: ['тринадцать'],
    14: ['четырнадцать'],
    15: ['пятнадцать'],
    16: ['шестнадцать'],
    17: ['семнадцать'],
    18: ['восемнадцать'],
    19: ['девятнадцать'],
    20: ['двадцать'],
    30: ['тридцать'],
    40: ['сорок'],
    50: ['пятьдесят']
}

y = input('To enter the time yourself print "Y" and press Enter or press Enter to use current time:\n')

if y != "y":
    h = int(datetime.datetime.now().strftime('%I'))
    m = int(datetime.datetime.now().strftime('%M'))
else:
    date_str = input("Please enter the time in hh:mm format:\n")
    date_obj = datetime.datetime.strptime(date_str, '%H:%M')
    x = int(date_obj.strftime('%I'))
    
    if x == 12:
        h = 0 
    else:
        h = x

    m = int(date_obj.strftime('%M'))

if m == 00:
    print(f"{d[h][0]} часа ровно")
elif m < 30: 
    print(f"{m} минут {d[h+1][1]}")
elif m == 30: 
    print(f"Половина {d[h+1][1]}")
elif m > 30 and m < 45:
    a = (m // 10) * 10
    b = m % 10
    print(f"{d[a][0]} {d[b][0]} минут {d[h+1][1]}")
elif m >= 45:
    a = 60 - m
    print(f"Без {d[a][0]} минут {d[h+1][1]}")













