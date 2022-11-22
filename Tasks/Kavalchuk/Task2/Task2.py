from datetime import datetime

answer = input("Введите время в формате hh:mm или нажмите 'Space', чтобы увидеть текущее время\n")

dict_hours = {1: ["один", "первого"],
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
              0: ["двенадцать", "двенадцатого"]}

dict_minutes = {1: ["одна", "одной"],
                2: ["две", "двух"],
                3: ["три", "трех"],
                4: ["четыре", "четырех"],
                5: ["пять", "пяти"],
                6: ["шесть", "шести"],
                7: ["семь", "семи"],
                8: ["восемь", "восьми"],
                9: ["девять", "девяти"],
                10: ["десять", "десяти"],
                11: ["одиннадцать", "одиннадцати"],
                12: ["двенадцать", "двенадцати"],
                13: ["тринадцать", "тринадцати"],
                14: ["четырнадцать", "четырнадцати"],
                15: ["пятнадцать", "пятнадцати"],
                16: ["шестнадцать"],
                17: ["семнадцать"],
                18: ["восемнадцать"],
                19: ["девятнадцать"],
                20: ["двадцать"],
                30: ["тридцать"],
                40: ["сорок"]}


def get_hours(hours, position):
    if hours == 12:
        hours = 0
    return dict_hours[hours][position]


def get_minutes(minutes, position):
    return dict_minutes[minutes][position]


def get_hours_end(hours):
    if hours == 1:
        return ""
    elif 1 < hours < 5:
        return "а"
    else:
        return "ов"


def get_minutes_end(minutes):
    if minutes == 1:
        return "а"
    elif 2 <= minutes <= 4:
        return "ы"
    elif 5 <= minutes <= 20 or minutes == 40:
        return ""


def is_valid_data(hours, minutes):
    if 0 <= hours <= 23 and 0 <= minutes <= 59:
        return True


def my_time(a: str):
    if a == " ":
        return list(map(int, datetime.now().strftime("%H:%M").split(":")))
    elif len(a) == 5 and a[2] == ":" and a[0:2].isdigit() and a[3:].isdigit():
        t = list(map(int, a.split(":")))
        if is_valid_data(t[0], t[1]):
            return t
        else:
            return []
    else:
        return []


def print_result(time):
    if time:
        if time[0] >= 12:
            time[0] -= 12

        match time:
            case [hours, minutes] if minutes == 0:
                print(f"{get_hours(hours, 0)} час{get_hours_end(hours)} ровно")
            case [hours, minutes] if minutes == 30:
                print(f"половина {get_hours(hours + 1, 1)}")
            case [hours, minutes] if minutes <= 20 or  minutes == 40:
                print(f"{get_minutes(minutes, 0)} минут{get_minutes_end(minutes)} {get_hours(hours + 1, 1)}")
            case [hours, minutes] if 20 < minutes < 45:
                m = minutes % 10
                print(f"{get_minutes(minutes - m, 0)} {get_minutes(m, 0)} минут{get_minutes_end(m)} {get_hours(hours + 1, 1)}")
            case [hours, minutes] if minutes >= 45:
                print(f"без {get_minutes(60 - minutes, 1)} минут {get_hours(hours + 1, 1)}")

    else:
        print("Неверный формат данных")


print_result(my_time(answer))
