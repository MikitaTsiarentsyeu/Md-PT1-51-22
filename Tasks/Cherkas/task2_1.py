import datetime

d = {1:['одна','первого', 'один', 'одной'],
     2:['две', 'второго', 'два', 'двух'],
    3:['три', 'третьего', 'трех'], 4:['четыре', 'четвертого', 'четырех'], 5:['пять', 'пятого', 'пяти'], 6: ['шесть', 'шестого', 'шести'],
     7:['семь', 'седьмого', 'семи'],8:['восемь', 'восьмого', 'восьми'],9:['девять', 'девятого', 'девяти'], 0:['ноль'],
     10:['десять', 'десятого', 'десяти'],
     11:['одинадцать', 'одиннадцатого', 'одиннадцати'],12:['двенадцать', 'двенадцатого', 'двенадцати'],
     'hour':['час', 'часа', 'часов'], 'minute':['минута', 'минуты', 'минут'],
     13:['тринадцать', 'тринадцати'], 14:['четырнадцать', 'четырнадцати'], 15:['пятнадцать', 'пятнадцати'],
     16:['шестнадцать'], 17:['семнадцать'], 18:['восемнадцать'],
     19:['девятнадцать'], 20:['двадцать'], 30:'тридцать', 40:'сорок'

     }
while True:
    answer = input("Если хотите ввести время самостоятельно, нажмите 0\nЕсли воспользоваться текущим, нажмите 1\n" )
    if answer != '1' and answer != '0':
        print('Неправильный ввод')
        continue
    break
if answer =='1':
 hours, minutes = datetime.datetime.now().hour, datetime.datetime.now().minute

elif answer == '0':
    while True:
        h_m = input('Введите время в формате hh:mm\n')
        if len(h_m) != 5:
            print('Неверная длинна ввода')
            continue
        if h_m[2] != ':':
            print('Неверный ввод')
            continue
        values = h_m.split(':')
        hours, minutes = values[0], values[1]
        if not (hours.isdigit() and  minutes.isdigit()):
            print('Неверный ввод. Введите цифры')
            continue
        hours, minutes = int(hours), int(minutes)
        if hours > 23 or minutes > 59:
            print('Неверный ввод')
            continue

        break




if minutes == 0:
    if hours == 1 or hours == 13:
        num = d[1][2]
        h= d['hour'][0]
    elif hours in (2, 14):
        num = d[2][2]
        h = d['hour'][1]
    elif hours in ( 3, 4, 15, 16):
        num = d[hours][0] if hours < 10 else d[hours-12][0]
        h= d['hour'][1]
    else:
        num = d[hours][0] if hours < 13 else d[hours - 12][0]
        h = d['hour'][2]
    print(f'{num} {h} ровно')



elif minutes == 30:
    num = d[(hours) + 1][1] if  hours < 12 else d[(hours) - 11][1]
    print(f'половина {num}')

elif minutes < 30:
    num = d[(hours) + 1][1] if hours < 12 else d[(hours) - 11][1]
    num_1 = d[minutes][0] if minutes < 21 else d[minutes - 20][0]
    if minutes in (1, 2, 3, 4, 21, 22, 23,24):
        min = d['minute'][0] if minutes in (1, 21) else d['minute'][1]
    else:
        min = d['minute'][2]
    print(f'{num_1} {min} {num}') if minutes < 21 else print(f'{d[20][0]} {num_1} {min} {num}')


elif 30 < minutes < 45:
    num = d[(hours) + 1][1] if hours < 12 else d[(hours) - 11][1]
    num_1 = d[minutes-30][0] if minutes < 40 else d[minutes - 40][0]
    if minutes == 40:
        num_1 = ''
    if minutes in (31, 32,33, 34, 41, 42, 43, 44):
        min = d['minute'][0] if minutes in (31, 41) else d['minute'][1]
    else:
        min = d['minute'][2]
    print(f'{d[30]} {num_1} {min} {num}') if minutes < 40 else print(f'{d[40]} {num_1} {min} {num}')


elif minutes >= 45:
    num_1 = d[60-minutes][-1]
    if hours  == 0 or hours  == 12:
        num = d['hour'][0]
    elif hours  == 1 or hours  == 13:
        num = d[2][2]
    else:
        num = d[hours+1][0] if hours < 12 else d[hours-11][0]
    print(f'без {num_1} {d["minute"][1] if minutes== 59 else d["minute"][2]} {num}')
