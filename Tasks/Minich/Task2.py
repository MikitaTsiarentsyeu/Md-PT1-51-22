import datetime
import re

digitsstr = ['0','1','2','3','4','5','6','7','8','9']
one = ['один','час','одна','минута','первого','','одной']
two = ['два','часа','две','минуты','второго',"двадцать",'двух']
three = ['три','часа','три','минуты','третьего','тридцать','трех']
four = ['четыре','часа','четыре','минуты','четвертого','сорок','четырех']
five = ['пять','часов','пять','минут','пятого','','пяти']
six = ['шесть','часов','шесть','минут','шестого','','шести']
seven = ['семь','часов','семь','минут','седьмого','','семи']
eight = ['восемь','часов','восемь','минут','восьмого','','восьми']
nine = ['девять','часов','девять','минут','девятого','','девяти']
zero = ['ноль','часов','','минут','','','']
ten = ['десять','часов','десять','минут','десятого','','десяти']
eleven = ['одиннадцать','часов','одиннадцать','минут','одиннадцатого','','одиннадцати']
twelve = ['двенадцать','часов','двенадцать','минут','','','двенадцати']
thirteen = ['тринадцать','часов','тринадцать','минут','','','тринадцати']
fourteen = ['четырнадцать','часов','четырнадцать','минут','','','четырнадцати']
fifteen = ['пятнадцать','часов','пятнадцать','минут','','','пятнадцати']
sixteen = ['шестнадцать','часов','шестнадцать','минут','','','']
seventeen = ['семнадцать','часов','семнадцать','минут','','','']
eighteen = ['восемнадцать','часов','восемнадцать','минут','','','']
nineteen = ['девятнадцать','часов','девятнадцать','минут','','','']
twenty = ['двадцать','часов','восемь','двадцать','минут','','','']


digitsdic = {1:one,2:two,3:three,4:four,5:five,6:six,7:seven,8:eight,9:nine,0:zero,10:ten,11:eleven,12:twelve,13:thirteen,15:fifteen,16:sixteen,17:seventeen,18:eighteen,19:nineteen,20:twenty}

x = datetime.datetime.now().strftime('%X')

timestr = input("Please enter 'Y' to enter the time manually, otherwise current time automatically\n")

if (timestr=='Y') or (timestr=='y'):

    #Attention! Enter the time in hh:mm format. Example 09:00, 23:32

    timestr = input('Enter time in hh:mm format\n')

    if len(str(timestr))==5:
        lis = []
        lis.extend(timestr)

        if (lis[0] in digitsstr) and (lis[1] in digitsstr) and (lis[3] in digitsstr) and (lis[4] in digitsstr):
        
            if lis[2]==':':
                k=1
            else:
                print('Wrong format')

            if int(lis[0]+lis[1])>23:
                print('Invalid clock format')

            if int(lis[3]+lis[4])>60:
                print('Invalid clock format')

        else:
            print('Wrong format') 

    else:
        print('Wrong format')

else:
    timestr = datetime.datetime.now().strftime('%X')
    lis = []
    lis.extend(timestr)
    lis = (lis[0:5])
    k=1

if k==1:
    hour = int(lis[0]+lis[1])
    minuts = int(lis[3]+lis[4])
    if minuts==0:
        if hour>12:
            hour = hour - 12
        result = digitsdic[hour][0] + ' ' + digitsdic[hour][1] + " ровно"
    elif minuts<30:
        hour = hour+1
        if hour>12:
            hour = hour - 12
        if minuts%20!=0 and minuts>20:
            result = digitsdic[20][0] + ' ' + digitsdic[minuts%20][2] + ' ' + digitsdic[minuts%20][3] + ' ' + digitsdic[hour][4]
        else:
            result = digitsdic[minuts][0] + ' ' + digitsdic[minuts][3] + ' ' + digitsdic[hour][4]
    elif minuts==30:    
        hour = hour+1
        if hour>12:
            hour = hour - 12
        result = 'половина ' + digitsdic[hour][4]
    elif minuts>30 and minuts<45:
        hour = hour+1
        if hour>12:
            hour = hour - 12
        result = digitsdic[int(minuts/10)][5] + ' ' + digitsdic[int(lis[4])][2] + ' ' + digitsdic[int(lis[4])][3] + ' ' + digitsdic[hour][4]
    else:
        hour = hour+1
        if hour>12:
            hour = hour - 12
        result = "без " + digitsdic[60-minuts][6] + ' ' + digitsdic[hour][4]
    print(result)
