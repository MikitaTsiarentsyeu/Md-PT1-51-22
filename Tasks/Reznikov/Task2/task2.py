from datetime import datetime as dt
import os
HOURS = (
    (u'один', u'первого'),
    (u'два', u'второго'),
    (u'три', u'третьего'),
    (u'четыре', u'четвертого'),
    (u'пять', u'пятого'),
    (u'шесть', u'шестого'),
    (u'семь', u'седьмого'),
    (u'восемь', u'восьмого'),
    (u'девять', u'девятого'),
    (u'десять', u'десятого'),
    (u'одинадцать', u'одиннадцатого'),
    (u'двенадцать', u'двенадцатого'),
)

MINUTES = (
    ('одна', 'одной'),
    ('две', 'двух'),
    ('три', 'трех'),
    ('четыре', 'четырёх'),
    ('пять', 'пяти'),
    ('шесть', 'шести'),
    ('семь', 'семи'),
    ('восемь', 'восьми'),
    ('девять', 'девяти'),
    ('десять', 'десяти'),
    ('одиннадцать', 'одиннадцати'),
    ('двенадцать', 'двенадцати'),
    ('тринадцать', 'тринадцати'),
    ('четырнадцать', 'четырнадцати'),
    ('пятнадцать', 'пятнадцати'),
    ('шестнадцать', 'шестнадцати'),
    ('семнадцать', 'семнадцати'),
    ('восемнадцать', 'восемнадцати'),
    ('девятнадцать', 'девятнадцати'),
)

TENS = (
    ('двадцать'),
    ('тридцать'),
    ('сорок'),
    ('пятьдесят')
)
def separate(mins):
    ten = mins // 10
    num = mins % 10

    return ten, num

def check_time(hours, mins):
    
    if mins == 0:
        str = f'{HOURS[hours-1][0]} часа ровно'
    
    elif mins < 30:
        ten, num = separate(mins)

        str = f'{MINUTES[mins-1][0] if mins < 20 else f"{TENS[ten-2]} {MINUTES[num-1][0]}"} минут(а/ы) {HOURS[hours][1] if hours != 12 else HOURS[0][1]}'
    elif mins == 30:
        str = f'половина {HOURS[hours][1] if hours != 12 else HOURS[0][1]}'
    elif 30 < mins < 45:
        ten, num = separate(mins)

        str = f'{TENS[ten-2]} {MINUTES[num-1][0]} минут(а/ы) {HOURS[hours][1] if hours != 12 else HOURS[0][1]}'
    elif mins >= 45:
        index = 60 - mins

        str = f'без {MINUTES[index-1][1]} минут(а/ы) {HOURS[hours][1] if hours != 12 else HOURS[0][1]}'

    os.system('cls')
    print('Время: ' + str + '\n\n')
    main()

def main():
    menu_title = input(
        'Please choose the required action:\
        \n1. Current time\
        \n2. User input time\n'
    )

    if menu_title == '1':
        
        time = dt.now()\
                    .strftime("%I:%M")

        hours, mins = time.split(':')

        check_time(int(hours), int(mins))
    elif menu_title == '2':
        os.system('cls')
        time = input('Please enter time in format HH:MM: ')
        if len(time) != 5 \
                    or ':' not in time \
                        or time.split(':')[0].isdigit() == False or time.split(':')[1].isdigit() == False \
                            or int(time.split(':')[0]) >= 24 or int(time.split(':')[0]) < 0 \
                                or int(time.split(':')[1]) >= 60 or int(time.split(':')[0]) < 0:
              
            return print('Invalid input date, try again...'), main()


        hours, mins = dt.strptime(time,'%H:%M')\
                            .strftime("%I:%M")\
                                .split(':')

        check_time(int(hours), int(mins))
    else:
        return print('Invalid input, try again...'), main()

if __name__ == "__main__":
    main()
