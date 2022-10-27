# Into Russian time  converter
# It has no validation check for inputed time but can translate 24-h format into 12-h format.

import datetime as dat


h_numb_dict = {1: ['час', 'первого'], 2: ['два', 'второго'], 3: ['три', 'третьего'], 4: ['четыре', 'четвёртого'],
               5: ['пять', 'пятого'], 6: ['шесть', 'шестого'], 7: ['семь', 'седьмого'], 8: ['восемь', 'восьмого'],
               9: ['девять', 'девятого'], 10: ['десять', 'десятого'], 11: ['одиннадцать', 'одиннадцатого'], 12: ['двенадцать', 'двенадцатого']}
m_numb_dict = {1: ['одна', 'одной'], 2: ['две', 'двух'], 3: ['три', 'трёх'], 4: ['четыре', 'четырёх'], 5: ['пять', 'пяти'],
               6: ['шесть', 'шести'], 7: ['семь', 'семи'], 8: ['восемь', 'восьми'], 9: ['девять', 'девяти'],
               10:['десять', 'десяти'], 11: ['одиннадцать', 'одиннадцати'], 12: ['двенадцать', 'двенадцати'],
               13: ['тринадцать', 'тринадцати'], 14: ['четырнадцать', 'четырнадцати'], 15: ['пятнадцать', 'пятнадцати'],
               16: ['шестнадцать', 'шестнадцати'], 17: ['семнадцать', 'семнадцати'], 18: ['восемнадцать', 'восемнадцати'],
               19: ['девятнадцать', 'девятнадцати'], 20: ['двадцать', 'двадцати'], 21: ['двадцать одна', 'двадцати одной'],
               22: ['двадцать две', 'двадцати двух'], 23: ['двадцать три', 'двадцати трёх'],
               24: ['двадцать четыре', 'двадцати четырёх'], 25: ['двадцать пять', 'двадцати пяти'],
               26: ['двадцать шесть', 'двадцати шести'], 27: ['двадцать семь', 'двадцати семи'],
               28: ['двадцать восемь', 'двадцати восьми'], 29: ['двадцать девять', 'двадцати девяти'], 30: ['тридцать'],
               31: ['тридцать одна'], 32: ['тридцать две'], 33: ['тридцать три'], 34: ['тридцать четыре'], 35: ['тридцать пять'],
               36: ['тридцать шесть'], 37: ['тридцать семь'], 38: ['тридцать восемь'], 39: ['тридцать девять'], 40: ['сорок'],
               41: ['сорок одна'], 42: ['сорок две'], 43: ['сорок три'], 44: ['сорок четыре']}
hours_list = ['часа', 'часов']
minutes_list = ['минута', 'минуты', 'минут']

print ('\nWelcome to "Into Russian time converter"!\n')
inp_time = ''
while inp_time != '1' and inp_time != '2':
    inp_time = input('Do you wish to:\n1. Use current time \n2. Enter your own?\n(enter 1 or 2)\n')
    if inp_time == '1':
        time_in = f'{dat.datetime.now().hour}:{dat.datetime.now().minute}'
    elif inp_time == '2':
        time_in = input('Enter your time in  hh:mm format please.\n')
    else:
        print('The entered symbol is not correct.\nChoose an option below.\n')

time_list = time_in.split(':')
hours = int(time_list[0])
hours = hours if hours <= 12 else hours - 12
minutes = int(time_list[1])
check_minutes = minutes if minutes < 45 else 60 - minutes

if hours == 1:                                  # get forms of hour word to final expressions
    h_word = ''
elif hours > 1 and hours < 5:
    h_word = hours_list[0]
else:
    h_word = hours_list[1]

if str(check_minutes)[-1] == '1':               # get forms of minute word to final expressions
    c_min_word = minutes_list[1]
else:
    c_min_word = minutes_list[2]

if minutes > 10 and minutes < 20:
    min_word = minutes_list[2]
elif str(minutes)[-1] == '1':
    min_word = minutes_list[0]
elif str(minutes)[-1] in ('2', '3', '4'):
    min_word = minutes_list[1]
else:
    min_word = minutes_list[2]

if minutes == 0:
    answer = f'{h_numb_dict[hours][0] if hours != 0 else h_numb_dict[12][0]} {h_word} ровно'.capitalize()
elif minutes > 0 and minutes < 5:
    answer = f'{m_numb_dict[minutes][0]} {min_word} {h_numb_dict[hours + 1 if hours < 12 else hours - 11][1]}'.capitalize()
elif minutes == 30:
    answer = f'половина {h_numb_dict[hours + 1 if hours < 12 else hours - 11][1]}'.capitalize()
elif minutes >= 45:
    answer = f'без {m_numb_dict[60-minutes][1]} {c_min_word} {h_numb_dict[hours + 1 if hours < 12 else hours - 11][0]}'.capitalize()
else:
    answer = f'{m_numb_dict[minutes][0]} {min_word} {h_numb_dict[hours + 1 if hours < 12 else hours - 11][1]}'.capitalize()


print(answer)
input('Press anything to quit.\n')