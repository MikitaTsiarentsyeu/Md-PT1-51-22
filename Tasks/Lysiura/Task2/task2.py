from datetime import datetime
answer = int(input("Do you want to enter time or read current time? (1/2)? :"))

if answer == 1:
    time = input("Введите время (hh:mm): ")
    chosen_hours = int(time.split(':')[0])
    chosen_minutes = int(time.split(':')[1])


    dict = {0:"ноль", 1:["один","второго","два", "одна"],2:["два","третьего","три", "две"],
        3:["три","четвертого", "четыре"],4:["четыре","пятого", "пять"],5:["пять","шестого", "шесть"], 
        6:["шесть", "седьмого", "семь"],7:["семь","восьмого", "восемь"],8:["восемь","девятого", "девять"],9:["девять","десятого", "десять"],
        10:["десять","одиннадцатого", "одинадцать"], 11:["одиннадцать","двенадцатого", "двенадцать"],12:["двенадцать","тринадцатого","первого"," ", "час"],
        13:["тринадцать","четырнадцатого","второго","час", "два"],14:["четырнадцать","пятнадцатого","третьего","два", "три"],
        15:["пятнадцать","шестнадцатого","четвертого","три", "четыре"], 16:["шестнадцать","семнадцатого","пятого","четыре", "пять"],
        17:["семнадцать","восемнадцатого","шестого","пять", "шесть"],
        18:["восемнадцать","девятнадцатого","седьмого","шесть", "семь"],19:["девятнадцать","двадцатого","восьмого","семь", "восемь"],
        20:["двадцать","двадцать первого","девятого","восемь", "девять"], 21:["двадцать одна","двадцать второго","десятого","девять", "десять"],
        22:["двадцать две","двадцать третьего","одиннадцатого","десять", "одинадцать"],23:["двадцать три","двадцати четвертого","двенадцатого","одинадцать", "двенадцать"],
        24:["двадцать четыре","","","двенадцать"],25:["двадцать пять"], 26:["двадцать шесть"],
        27:["двадцать семь"],28:["двадцать восемь"],29:["двадцать девять"],
        30:["тридцать"], 31:["тридцать одна"],32:["тридцать две"],
        33:["тридцать три"],34:["тридцать четыре"],35:["тридцать пять"], 
        36:["тридцать шесть"],37:["тридцать семь"],38:["тридцать восемь"],
        39:["тридцать девять"],
        40:["сорок"], 41:["сорок одна"],42:["сорок две"],43:["сорок три"],
        44:["сорок четыре"],45:["сорок пять","пятнадцати"], 46:["сорок шесть","четырнадцати"],
        47:["сорок семь","тринадцати"],48:["сорок восемь","двенадцати"],49:["сорок девять","одиннадцати"],
        50:["пятьдесят","десяти"], 51:["пятьдесят одна","девяти"],52:["пятьдесят две","восьми"],
        53:["пятьдесят три","семи"],54:["пятьдесят четыре","шести"],55:["пятьдесят пять","пяти"], 
        56:["пятьдесят шесть","четырех"],57:["пятьдесят семь","трех"],58:["пятьдесят восемь","двух"],
        59:["пятьдесят девять","одной"],
        00:["","первого", "час"]
        }
    if chosen_hours < 24 and chosen_minutes <60:
        if chosen_hours in dict and chosen_minutes in dict and chosen_minutes == 00:
            if chosen_hours == 00:
                (print("двенадцать часов ровно"))
                
            elif chosen_hours < 13:
                minutes_n = dict[chosen_minutes]
                hours_n = dict[chosen_hours]
                print(f'{hours_n[0]} ровно ')
    
            else:
                minutes_n = dict[chosen_minutes]
                hours_n = dict[chosen_hours]
                print(f'{hours_n[3]} ровно ')
       
        
        elif chosen_hours in dict and chosen_minutes in dict and chosen_minutes == 30:
        
            if chosen_hours <13 or chosen_hours == 00:
                minutes_n = dict[chosen_minutes]
                hours_n = dict[chosen_hours]
                print(f'половина {hours_n[1]} ')
            else:
                minutes_n = dict[chosen_minutes]
                hours_n = dict[chosen_hours]
                print(f'половина {hours_n[2]}  ')
            
        elif chosen_hours in dict and chosen_minutes in dict and chosen_minutes < 30:
            if chosen_minutes == 1 or chosen_minutes == 2:
                minutes_n = dict[chosen_minutes]
                hours_n = dict[chosen_hours]
                print(f'{minutes_n[3]} минут(ы/а) {hours_n[2]}  ')
            
            elif chosen_hours <13 or chosen_hours == 00:
                minutes_n = dict[chosen_minutes]
                hours_n = dict[chosen_hours]
                print(f'{minutes_n[0]} минут(ы/а) {hours_n[1]}  ')
            else:
                minutes_n = dict[chosen_minutes]
                hours_n = dict[chosen_hours]
                print(f'{minutes_n[0]} минут(ы/а) {hours_n[2]}  ')
   
        elif chosen_hours in dict and chosen_minutes in dict and chosen_minutes > 30 and chosen_minutes < 45:
                if chosen_hours <13 or chosen_hours == 00:
                    minutes_n = dict[chosen_minutes]
                    hours_n = dict[chosen_hours]
                    print(f'{minutes_n[0]} минут(ы/а) {hours_n[2]}  ')
                else:
                    minutes_n = dict[chosen_minutes]
                    hours_n = dict[chosen_hours]
                    print(f'{minutes_n[0]} минут(ы/а) {hours_n[2]}  ')
   
        elif chosen_hours in dict and chosen_minutes in dict and chosen_minutes >= 45 and chosen_minutes< 60:
                if chosen_hours <13 or chosen_hours == 00:
                    minutes_n = dict[chosen_minutes]
                    hours_n = dict[chosen_hours]
                    print(f' без {minutes_n[1]} минут(ы/а) {hours_n[2]}   ')
                else: 
                    minutes_n = dict[chosen_minutes]
                    hours_n = dict[chosen_hours]
                    print(f'без {minutes_n[1]} минут(ы/а) {hours_n[4]} ')
    
    else:
        print("Неверные данные")
if answer == 2:
    current_date = str(datetime.today())
    print(current_date)
    current_time = current_date[11:16]
    print(current_time)
    hours = int(current_time.split(':')[0])
    minutes = int(current_time.split(':')[1])
    
    dict = {0:"ноль", 1:["один","второго","два", "одна" ],2:["два","третьего","три", "две"],
        3:["три","четвертого", "четыре"],4:["четыре","пятого", "пять"],5:["пять","шестого", "шесть"], 
        6:["шесть", "седьмого", "семь"],7:["семь","восьмого", "восемь"],8:["восемь","девятого", "девять"],9:["девять","десятого", "десять"],
        10:["десять","одиннадцатого", "одинадцать"], 11:["одиннадцать","двенадцатого", "двенадцать"],12:["двенадцать","тринадцатого","первого"," ", "час"],
        13:["тринадцать","четырнадцатого","второго","час", "два"],14:["четырнадцать","пятнадцатого","третьего","два", "три"],
        15:["пятнадцать","шестнадцатого","четвертого","три", "четыре"], 16:["шестнадцать","семнадцатого","пятого","четыре", "пять"],
        17:["семнадцать","восемнадцатого","шестого","пять", "шесть"],
        18:["восемнадцать","девятнадцатого","седьмого","шесть", "семь"],19:["девятнадцать","двадцатого","восьмого","семь", "восемь"],
        20:["двадцать","двадцать первого","девятого","восемь", "девять"], 21:["двадцать одна","двадцать второго","десятого","девять", "десять"],
        22:["двадцать две","двадцать третьего","одиннадцатого","десять", "одинадцать"],23:["двадцать три","двадцати четвертого","двенадцатого","одинадцать", "двенадцать"],
        24:["двадцать четыре","","","двенадцать"],25:["двадцать пять"], 26:["двадцать шесть"],
        27:["двадцать семь"],28:["двадцать восемь"],29:["двадцать девять"],
        30:["тридцать"], 31:["тридцать одна"],32:["тридцать две"],
        33:["тридцать три"],34:["тридцать четыре"],35:["тридцать пять"], 
        36:["тридцать шесть"],37:["тридцать семь"],38:["тридцать восемь"],
        39:["тридцать девять"],
        40:["сорок"], 41:["сорок одна"],42:["сорок две"],43:["сорок три"],
        44:["сорок четыре"],45:["сорок пять","пятнадцати"], 46:["сорок шесть","четырнадцати"],
        47:["сорок семь","тринадцати"],48:["сорок восемь","двенадцати"],49:["сорок девять","одиннадцати"],
        50:["пятьдесят","десяти"], 51:["пятьдесят один","девяти"],52:["пятьдесят два","восьми"],
        53:["пятьдесят три","семи"],54:["пятьдесят четыре","шести"],55:["пятьдесят пять","пяти"], 
        56:["пятьдесят шесть","четырех"],57:["пятьдесят семь","трех"],58:["пятьдесят восемь","двух"],
        59:["пятьдесят девять","одной"],
        00:["","первого", "один"]
        }
    
    if hours < 24 and minutes <60:
        if hours in dict and minutes in dict and minutes == 00:
            if hours == 00:
                (print("двенадцать часов ровно"))
    
            elif hours < 13:
                minutes_n = dict[minutes]
                hours_n = dict[hours]
                print(f'{hours_n[0]} ровно ')
    
            else:
                minutes_n = dict[minutes]
                hours_n = dict[hours]
                print(f'{hours_n[3]} ровно ')
       
        
        elif hours in dict and minutes in dict and minutes == 30:
        
            if hours <13 or hours == 00:
                minutes_n = dict[minutes]
                hours_n = dict[hours]
                print(f'половина {hours_n[1]} ')
            else:
                minutes_n = dict[minutes]
                hours_n = dict[hours]
                print(f'половина {hours_n[2]}  ')
            
        elif hours in dict and minutes in dict and minutes < 30:
            if minutes == 1 or minutes == 2:
                minutes_n = dict[minutes]
                hours_n = dict[hours]
                print(f'{minutes_n[3]} минут(ы/а) {hours_n[2]}  ')
            
            elif hours <13 or hours == 00:
                minutes_n = dict[minutes]
                hours_n = dict[hours]
                print(f'{minutes_n[0]} минут(ы/а) {hours_n[1]}  ')
            else:
                minutes_n = dict[minutes]
                hours_n = dict[hours]
                print(f'{minutes_n[0]} минут(ы/а) {hours_n[2]}  ')
   
        elif hours in dict and minutes in dict and minutes > 30 and minutes < 45:
                if hours <13 or hours == 00:
                    minutes_n = dict[minutes]
                    hours_n = dict[hours]
                    print(f'{minutes_n[0]} минут(ы/а) {hours_n[2]}  ')
                else:
                    minutes_n = dict[minutes]
                    hours_n = dict[hours]
                    print(f'{minutes_n[0]} минут(ы/а) {hours_n[2]}  ')
   
        elif hours in dict and minutes in dict and minutes >= 45 and minutes< 60:
                if hours <13 or hours == 00:
                    minutes_n = dict[minutes]
                    hours_n = dict[hours]
                    print(f' без {minutes_n[1]} минут(ы/а) {hours_n[2]}   ')
                else: 
                    minutes_n = dict[minutes]
                    hours_n = dict[hours]
                    print(f'без {minutes_n[1]} минут(ы/а) {hours_n[4]} ')
    
    else:
        print("Неверные данные")