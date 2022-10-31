from datetime import *
import locale

locale.getlocale(category=2)
('Russian_Russia', '1251')

dict_hours = {1: ["час", "первого"],
              2: ["два", "второго"],
              3: ["три", "третьего"],
              4: ["четыре", "четвертого"],
              5: ["пять", "пятого"],
              6: ["шесть", "шестого"],
              7: ["семь", "седьмого"],
              8: ["восемь", "восьмого"],
              9: ["девять", "девятого"],
              10: ["десять", "десятого"],
              11: ["одиннадцать", "одиннадцатого"],
              12: ["двенадцать", "двенадцатого"]}

dict_minutes = {1:["одна", "одной"], 2:["две", "двух"], 3:["три", "трех"], 4:["четыре", "четырех"],
                5:["пять", "пяти"], 6:["шесть", "шести"], 7:["семь", "семи"], 8:["восемь", "восьми"],
                9:["девять", "девяти"], 10:["десять", "десяти"], 11:["одиннадцать", "одиннадцати"],
                12:["двенадцать", "двенадцати"], 13:["тринадцать", "тринадцати"],
                14:["четырнадцать", "четырнадцати"], 15:["пятнадцать", "пятнадцати"], 16:["шестнадцать"],
                17:["семнадцать"], 18:["восемнадцать"], 19:["девятнадцать"], 20:["двадцать", "двадцати"],
                21:["двадцать одна"], 22:["двадцать две"], 23:["двадцать три"], 24:["двадцать четыре"],
                25:["двадцать пять"], 26:["двадцать шесть"], 27:["двадцать семь"], 28:["двадцать восемь"],
                29:["двадцать девять"], 30:["тридцать"], 31:["тридцать одна"], 32:["тридцать две"],
                33:["тридцать три"], 34:["тридцать четыре"], 35:["тридцать пять"], 36:["тридцать шесть"],
                37:["тридцать семь"], 38:["тридцать восемь"], 39:["тридцать девять"], 40:["сорок"],
                41:["сорок одна"], 42:["сорок две"], 43:["сорок три"], 44:["сорок четыре"]}

list_hours = ['часа', 'часов']
list_minutes = ['минута', 'минуты', 'минут']

def time_counter(user_time = str):

    user_time = user_time.split(":")
    hour_ru = int(user_time[0])
    minutes_ru = int(user_time[1])
  
    hour_ru = hour_ru if 0 <= hour_ru <= 12 else abs(hour_ru - 12)

    if minutes_ru == 0:
        if 1 < hour_ru < 5:
            user_time_ru = f'{hour_ru}:{minutes_ru} - {dict_hours[hour_ru][0]} {list_hours[0]} ровно'
        elif 4 < hour_ru < 12:
            user_time_ru = f'{hour_ru}:{minutes_ru} - {dict_hours[hour_ru][0]} {list_hours[1]} ровно'

    elif minutes_ru < 30:
        if minutes_ru == 1 or minutes_ru == 21:
            user_time_ru = f'{hour_ru}:{minutes_ru} - {dict_minutes[minutes_ru][0]} {list_minutes[0]} {dict_hours[hour_ru+1][1]}'
        elif 1 < minutes_ru < 5 or 21 < minutes_ru < 25:
            user_time_ru = f'{hour_ru}:{minutes_ru} - {dict_minutes[minutes_ru][0]} {list_minutes[1]} {dict_hours[hour_ru+1][1]}'
        elif 4 < minutes_ru < 21 or 24 < minutes_ru <30:
            user_time_ru = f'{hour_ru}:{minutes_ru} - {dict_minutes[minutes_ru][0]} {list_minutes[2]} {dict_hours[hour_ru+1][1]}'

    elif minutes_ru == 30:
        user_time_ru = f'{hour_ru}:{minutes_ru} - половина {dict_hours[hour_ru+1][1]}'

    elif 30  < minutes_ru  < 45:
        user_time_ru = f'{hour_ru}:{minutes_ru} - {dict_minutes[minutes_ru][0]} {list_minutes[2]} {dict_hours[hour_ru+1][1]}'
        if minutes_ru == 31 or minutes_ru == 41:
            user_time_ru = f'{hour_ru}:{minutes_ru} - {dict_minutes[minutes_ru][0]} {list_minutes[0]} {dict_hours[hour_ru+1][1]}'
        elif 32 <= minutes_ru <= 34 or 42 <= minutes_ru <= 44:
            user_time_ru = f'{hour_ru}:{minutes_ru} - {dict_minutes[minutes_ru][0]} {list_minutes[1]} {dict_hours[hour_ru+1][1]}'         
        elif 35 <= minutes_ru <= 40:
            user_time_ru = f'{hour_ru}:{minutes_ru} - {dict_minutes[minutes_ru][0]} {list_minutes[2]} {dict_hours[hour_ru+1][1]}' 

    elif minutes_ru >= 45:
      user_time_ru = f'{hour_ru}:{minutes_ru} - без {dict_minutes[60-minutes_ru][1]} {list_minutes[2]} {dict_hours[hour_ru+1][1]}'

    return user_time_ru

print("В программе вы можете вывести свое текущее время или ввести свое")
user_choice = input("Введите 1 - для вывода текущего времени и 2 - для ввода времени с клавиатуры\n")

if user_choice == "1" :
    time_now = datetime.now()
    user_time = str(time_now.strftime("%H:%M"))
    user_time_input = user_time
    print("Ваше время: ", time_counter(user_time_input))

elif user_choice == "2" :
    user_time = input("Введите время в формате чч:мм : \t")
    user_time_input = user_time
    print("Ваше время: ", time_counter(user_time_input))