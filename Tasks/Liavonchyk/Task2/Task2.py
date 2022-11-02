import datetime

# dictionaries
hours = {
    0: ['двенадцать', 'двенадцатого'],
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
    13: ['час', 'первого'],
    14: ['два', 'второго'],
    15: ['три', 'третьего'],
    16: ['четыре', 'четвертого'],
    17: ['пять', 'пятого'],
    18: ['шесть', 'шестого'],
    19: ['семь', 'седьмого'],
    20: ['восемь', 'восьмого'],
    21: ['девять', 'девятого'],
    22: ['десять', 'десятого'],
    23: ['одиннадцать', 'одиннадцатого']
}

minutes = {
    0: 'ровно',
    1: 'одна',
    2: 'две',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять',
    10: 'десять',
    11: 'одиннадцать',
    12: 'двенадцать',
    13: 'тринадцать',
    14: 'четырнадцать',
    15: 'пятнадцать',
    16: 'шестнадцать',
    17: 'семнадцать',
    18: 'восемнадцать',
    19: 'девятнадцать',
    20: 'двадцать',
    21: 'двадцать одна',
    22: 'двадцать две',
    23: 'двадцать три',
    24: 'двадцать четыре',
    25: 'двадцать пять',
    26: 'двадцать шесть',
    27: 'двадцать семь',
    28: 'двадцать восемь',
    29: 'двадцать девять',
    30: 'половина',
    31: 'тридцать одна',
    32: 'тридцать две',
    33: 'тридцать три',
    34: 'тридцать четыре',
    35: 'тридцать пять',
    36: 'тридцать шесть',
    37: 'тридцать семь',
    38: 'тридцать восемь',
    39: 'тридцать девять',
    40: 'сорок',
    41: 'сорок одна',
    42: 'сорок две',
    43: 'сорок три',
    44: 'сорок четыре',
    45: 'без пятнадцати',
    46: 'без четырнадцати',
    47: 'без тринадцати',
    48: 'без двенадцати',
    49: 'без одиннадцати',
    50: 'без десяти',
    51: 'без девяти',
    52: 'без восьми',
    53: 'без семи',
    54: 'без шести',
    55: 'без пяти',
    56: 'без четырех',
    57: 'без трех',
    58: 'без двух',
    59: 'без одной'
}

# lists for correct cases
hour_names = ['час','часа','часов']
minute_names = ['минута','минут','минуты']

now_time_answer = False
now_time = input("Вы хотите получить текущее время?\n")

# initialization
enter_time = ''
print_text = ''
in_hour = None
in_minute = None
error_text ='Неожиданно! Проверьте время, которое вы ввели: '

# check if we want to get current time
if now_time.lower() in ['yes','y','yeah','да','д','lf']:
    now_time_answer = True
    in_hour = datetime.datetime.now().hour
    in_minute = datetime.datetime.now().minute

# enter time if needed
if now_time_answer == False:
    enter_time = input("Введите время в формате hh:mm\n")
    if enter_time.__contains__(":"): # check if we can split time
        in_hour = int(enter_time.split(":")[0])
        in_minute = int(enter_time.split(":")[1])
    else :
        print_text = error_text + enter_time

# if we splitted the time correctly and time is in range
if in_hour != None and in_minute != None and ((0 <= in_minute < 60) and (0 <= in_hour < 24)):
    if in_minute == 0:
        if in_hour % 12 == 1:
            hour_name = hour_names[0]
        elif in_hour % 12 in [2, 3, 4]:
            hour_name = hour_names[1]
        else:
            hour_name = hour_names[2]
        print_text = f'{hours[in_hour][0].capitalize()} {hour_name} ровно'
    elif (0 < in_minute < 30) or (30 < in_minute < 45):
        if in_minute % 10 == 1 and in_minute != 11:
            minute_name = minute_names[0]
        elif in_minute % 10 in [2, 3, 4]:
            minute_name = minute_names[2]
        else:
            minute_name = minute_names[1]
        print_text = f'{minutes[in_minute].capitalize()} {minute_name} {hours[in_hour + 1 if in_hour < 23 else 0][1]}'
    elif in_minute == 30:
        print_text = f'Половина {hours[in_hour + 1 if in_hour < 23 else 0][1]}'
    elif 45 <= in_minute < 60:
        if in_minute == 59:
            minute_name = minute_names[2]
        else:
            minute_name = minute_names[1]
        print_text = f'{minutes[in_minute].capitalize()} {minute_name} {hours[in_hour + 1 if in_hour < 23 else 0][0]}'

# Notify if time is out of range
elif in_hour != None and in_minute != None and not ((0 <= in_minute < 60) and (0 <= in_hour < 24)):
    print_text = f"{error_text}{in_hour}:{in_minute}"

# output
print(print_text)



