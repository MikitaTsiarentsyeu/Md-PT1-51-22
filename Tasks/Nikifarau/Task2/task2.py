# min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
# min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
# min == 30: половина такого-то (15:30 - половина четвёртого)
# min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
# min >= 45 без min такого-то (08:54 - без шести минут девять)

import datetime

hour_real = int(datetime.datetime.now().hour)
minute_real =int(datetime.datetime.now().minute)

dir_hour = {0 : ("ноль часов", "первого", "час"), 1 : ("один час", "второго", "два"),
2 : ("два часа", "третьего", "три"), 3 : ("три часа", "четвертого", "четыре"), 4 : ("четыре часа", "пятого", "пять"),
5 : ("пять часов", "шестого", "шесть"),6 : ("шесть часов", "седьмого", "семь"),7 : ("семь часов", "восьмого", "восемь"),
8 : ("восемь часов", "девятого", "девять"), 9 : ("девять часов", "десятого", "десять"),
10 : ("десять часов", "одиннадцатого", "одиннадцать"), 11 : ("одиннадцать часов", "двенадцатого", "двенадцать"),
12 : ("двенадцать часов", "первого", "час"), 13 : ("один час", "второго", "два"), 14 : ("два часа", "третьего", "три"),
15 : ("три часа", "четвертого", "четыре"), 16 : ("четыре часа", "пятого", "пять"),
17 : ("пять часов", "шестого", "шесть"), 18 : ("шесть часов", "седьмого", "семь"),
19 : ("семь часов", "восьмого", "восемь"), 20 : ("восемь часов", "девятого", "девять"),
21 : ("девять часов", "десятого", "десять"), 22 : ("десять часов", "одиннадцатого", "одиннадцать"),
23 : ("одиннадцать часов", "двенадцатого", "двенадцать")}

dir_min = {0 : "ноль минут", 1 : "одна минута", 2 : "две минуты",3 : "три минуты", 4 : "четыре минуты",
5 : "пять минут", 6 : "шесть минут",7 : "семь минут", 8 : "восемь минут", 9 : "девять минут", 10 : "десять минут",
11 : "одиннадцать минут", 12 : "двенадцать минут",13 : "тринадцать минут", 14 : "четырнадцать минут",
15 : "пятнадцать минут", 16 : "шестнадцать минут", 17 : "семнадцать минут", 18 : "восемнадцать минут",
19 : "девятнадцать минут", 20 : "двадцать минут", 21 : "двадцать одна минута", 22 : "двадцать две минуты",
23 : "двадцать три минуты", 24 : "двадцать четыре минуты", 25 : "двадцать пять минут",
26 : "двадцать шесть минут", 27 : "двадцать семь минут", 28 : "двадцать восемь минут", 29 : "двадцать девять минут",
30 : "тридцать минут", 31 : "тридцать одна минута", 32 : "тридцать две минуты", 33 : "тридцать три минуты",
34 : "тридцать четыре минуты", 35 : "тридцать пять минут", 36 : "тридцать шесть минут", 37 : "тридцать семь минут",
38 : "тридцать восемь минут", 39 : "тридцать девять минут", 40 : "сорок минут", 41 : "сорок одна минута",
42 : "сорок две минуты", 43 : "сорок три минуты", 44 : "сорок четыре минуты", 45 : "без пятнадцати минут",
46 : "без четырнадцати минут ", 47 : " без тринадцати минут", 48 : "без двенадцати минут", 49 : "без одиннадцати минут",
50 : "без десяти минут", 51 : "без девяти минут", 52 : "без восьми минут", 53 : "без семи минут",54 : "без шести минут",
55 : "без пяти минут", 56 : "без четырех минут", 57 : "без трех минут", 58 : "без двух минут", 59 : "без одной минуты"}

change_time = None
while change_time not in [1, 2]:
    change_time = int(input(" Choose actual_time (1) or_your_time (2):\n"))

if change_time == 1 and minute_real == 0 and hour_real in dir_hour and minute_real in dir_min:
    hour = dir_hour[hour_real][0]
    min = dir_min[minute_real]
    print(f"result {hour} ровно реального времени")
    exit()

if change_time == 1 and 0 < minute_real < 30 and hour_real in dir_hour and minute_real in dir_min:
    hour = dir_hour[hour_real][1]
    min = dir_min[minute_real]
    print(f"result {min} {hour} реального времени")
    exit()

if change_time == 1 and minute_real == 30 and hour_real in dir_hour and minute_real in dir_min:
    hour = dir_hour[hour_real][1]
    min = dir_min[minute_real]
    print(f"result половина {hour} реального времени")
    exit()

if change_time == 1 and 30 < minute_real < 45 and hour_real in dir_hour and minute_real in dir_min:
    hour = dir_hour[hour_real][1]
    min = dir_min[minute_real]
    print(f"result {min} {hour} реального времени")
    exit()

if change_time == 1 and 44 < minute_real <= 59 and hour_real in dir_hour and minute_real in dir_min:
    hour = dir_hour[hour_real][2]
    min = dir_min[minute_real]
    print(f"result {min} {hour} реального времени")
    exit()

elif change_time == 2:
    your_time = input("Enter your time in format hh:mm :\n")
    your_time = your_time.replace(" ", '')
    if len(your_time) != 5 \
            or your_time[2] != ':':
        print("прошу вас ввести время правильно")
        exit()

    s_your_time = your_time.split(':')
    s_hour = None
    s_hour = int(s_your_time[0])
    s_min = int(s_your_time[1])

    if 0 < s_hour > 23:
        print("прошу вас ввести часы правильно")
        exit()
    if 0 < s_min > 59:
        print("прошу вас ввести минуты правильно")
        exit()

    if  s_min == 0 and s_hour in dir_hour and s_min in dir_min:
        k_hour = dir_hour[s_hour][0]
        k_min = dir_min[s_min]
        print(f"result {k_hour} ровно придуманного времени")
        exit()

    if  0 < s_min < 30 and s_hour in dir_hour and s_min in dir_min:
        k_hour = dir_hour[s_hour][1]
        k_min = dir_min[s_min]
        print(f"result {k_min} {k_hour} придуманного времени")
        exit()

    if  s_min == 30 and s_hour in dir_hour and s_min in dir_min:
        k_hour = dir_hour[s_hour][1]
        k_min = dir_min[s_min]
        print(f"result половина {k_hour} придуманного времени")
        exit()

    if  30 < s_min < 45 and s_hour in dir_hour and s_min in dir_min:
        k_hour = dir_hour[s_hour][1]
        k_min = dir_min[s_min]
        print(f"result {k_min} {k_hour} придуманного времени")
        exit()

    if  44 < s_min <= 59 and s_hour in dir_hour and s_min in dir_min:
        k_hour = dir_hour[s_hour][2]
        k_min = dir_min[s_min]
        print(f"result {k_min} {k_hour} придуманного времени")
        exit()

else : print("Big mistake")
