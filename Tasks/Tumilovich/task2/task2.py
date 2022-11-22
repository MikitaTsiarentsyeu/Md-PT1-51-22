from datetime import datetime
option = int(input('Type 1 or 2:\n 1 - Current time\n 2 - Your time\n'))

d_hrs = {
    0:('двенадцать', 'двенадцатого'),
    1:('один','первого'),
    2:('два', 'второго'),
    3:('три','третьего'),
    4:('четыре','четвёртого'),
    5:('пять','пятого'),
    6:('шесть','шестого'),
    7:('семь', 'седьмого'),
    8:('восемь', 'восьмого'),
    9:('девять', 'девятого'),
    10:('десять', 'десятого'),
    11:('одиннадцать','одиннадцатого'),
    12:('двенадцать', 'двенадцатого')}


d_mins = {
    0:('',),
    1:('одна', 'одной'),
    2:('две', 'двух'),
    3:('три','трёх'),
    4:('четыре','четырёх'),
    5:('пять','пяти'),
    6:('шесть','шести'),
    7:('семь','семи'),
    8:('восемь','восьми'),
    9:('девять','девяти'),
    10:('десять','десяти'),
    11:('одиннадцать','одиннадцати'),
    12:('двенадцать','двенадцати'),
    13:('тринадцать','тринадцати'),
    14:('четырнадцать','четырнадцати'),
    15:('пятнадцать','пятнадцати'),
    16:('шестнадцать'),
    17:('семнадцать',),
    18:('восемнадцать',),
    19:('девятнадцать',),
    20:('двадцать',),
    30:('тридцать',),
    40:('сорок',),
    50:('пятьдесят',) }

hrs_vers = ['час', 'часа', 'часов']
mins_vers = ['минута', 'минуты', 'минут']


if option == 1:
    hours = datetime.now().time().hour % 12
    mins = datetime.now().time().minute

if option == 2:
    while True:
        time = input('Enter your time in format hh:mm\n')

        if len(time) !=5:
            print('incorrect length')
            continue
        if time[2] != ':':
            print('You need to use ":"')
            continue
        time = time.split(':')
        if not (time[0].isdigit() and time[1].isdigit()):
            print('You need to use digits')
            continue
        if int(time[0]) > 24 or int(time[1]) > 59:
            print('Incorrect time')
            continue
        break


    hours = int(time[0]) % 12
    mins = int(time[1])



if mins not in d_mins:
    mins = str(mins)
    name_mins = d_mins[int((mins[0] + '0'))][0] + " " + d_mins[int(mins[1])][0]
    mins = int(mins)


if mins == 0:
    if hours == 1:
        hrs_vers = hrs_vers[0]
    elif hours in (2,3,4):
        hrs_vers = hrs_vers[1]
    else:
        hrs_vers = hrs_vers[2]

    print(f'{d_hrs[hours][0]} {hrs_vers} ровно')

elif 0 < mins < 30:
    if mins in (1, 21):
        mins_vers = mins_vers[0]
    elif mins in (2, 3, 4, 22, 23, 24):
        mins_vers = mins_vers[1]
    else:
        mins_vers = mins_vers[2]

    print(f'{d_mins[mins][0] if mins in d_mins else name_mins} {mins_vers} {d_hrs[hours + 1][1]}')


elif mins == 30:
    print(f'половина {d_hrs[hours + 1][1]}')


elif 30 < mins < 45:
    if mins in (31, 41):
        mins_ver = mins_vers[0]
    elif mins in (35, 36, 37, 38, 39, 40):
        mins_ver = mins_vers[2]
    else:
        mins_ver = mins_vers[1]


    print(f'{d_mins[mins][0] if mins in d_mins else name_mins} {mins_ver} {d_hrs[hours + 1][1]}')


elif mins >= 45:
    mins = 60 - mins
    print(f'без {d_mins[mins][1]} {"минут" if mins != 1 else "минуты"} {d_hrs[hours + 1][0]}')








