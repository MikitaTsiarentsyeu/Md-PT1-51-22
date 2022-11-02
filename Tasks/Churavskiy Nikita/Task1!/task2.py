from datetime import datetime
current_date = str(datetime.now().time())[0:5]

time_dict={ 
0:['двенадцать','двенадцать'], 1:['час', 'первого','одной'],2:['два', 'второго','двух'],3:['три', 'третьего','трех'],
4:['четыре', 'четвертого','четырех'],5:['пять', 'пятого','пяти'],6:['шесть', 'шестого','шести'],7:['семь', 'седьмого','семи'],
8:['восемь', 'восьмого','восьми'],9:['девять', 'девятого','девяти'], 10:['десять', 'десятого','десяти'],
11:['одинадцать', 'одинадцатого','одинадцати'],12:['двенадцать', 'двенадцатого','двенадцати'],13:['час','тринадцать','тринадцати'],
14:['два','четырнадцать','четырнадцати'],15:['три','пятнадцать','пятнадцати'],16:'шестнадцать', 17:'семнадцать',18:'восменадцать',
19:'девятнадцать',20:'двадцать',21:'двадцать одна', 22:'двадцать две',23:'двадцать три',24:'двадцать четыре',25:'двадцать пять',
26:'двадцать шесть',27:'двадцать семь',28:'двадцать восемь',29:'двадцать девять',31:'тридцать одна',32:'тридцать две',
33:'тридцать три',34:'тридцать четыре',35:'тридцать пять',36:'тридцать шесть',37:'тридцать семь',38:'тридцать восемь',
39:'тридцать девять',40:'сорок',41:'сорок одна',42:'сорок две',43:'сорок три',44:'сорок четыре',45:'сорок пять'
}

time=input('please enter your time in format hh:mm\nif you want look current time, return Y\n')
if time=='Y':
    print(current_date)
else:
    c=[int(i) for i in time.split(':')]
    hour=c[0]
    min=c[1]
    if min == 00:
        print(f'{hour}:{str(min)+str(0)} - {time_dict[hour][0]} часов ровно' 
        if hour<12 else f'{hour}:{str(min)+str(0)} - {time_dict[abs(12-(hour))][0]} часов ровно')
    elif min<=15:
        print(f'{hour}:{min} - {time_dict[min][0]} минут {time_dict[hour+1][1]}' 
        if hour<12 else f'{hour}:{min} - {time_dict[min][0]} минут {time_dict[abs(12-(hour+1))][1]}')
    elif 15<min<30:
        print(f'{hour}:{min} - {time_dict[min]} минут {time_dict[hour+1][1]}' 
        if hour<12 else f'{hour}:{min} - {time_dict[min]} минут {time_dict[abs(12-(hour+1))][1]}')
    elif min==30:
        print(f'{hour}:{min} - половина {time_dict[hour+1][1]}' 
        if hour<12 else f'{hour}:{min} - половина {time_dict[abs(12-(hour+1))][1]}')
    elif 30<min<=41:
        print(f'{hour}:{min} - {time_dict[min]} минут {time_dict[hour+1][1]}' 
        if hour<12 else f'{hour}:{min} - {time_dict[min]} минут {time_dict[abs(12-(hour+1))][1]}')
    elif 40<=min<=44:
        print(f'{hour}:{min} - {time_dict[min]} минуты {time_dict[hour+1][1]}' 
        if hour<12 else f'{hour}:{min} - {time_dict[min]} минуты {time_dict[abs(12-(hour+1))][1]}')
    elif min>=45:
        print(f'{hour}:{min} - без {time_dict[60-min][2]} минут {time_dict[hour+1][0]}' 
        if hour<12 else f'{hour}:{min} - без {time_dict[60-min][2]} минут {time_dict[abs(12-(hour+1))][0]}')
   


