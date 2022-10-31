import datetime

while True:
    while True:
        input_time = input(
            "Choose one of the options:\n1. Enter your time value in format 'HH:MM'.\n2. Press 'Enter' to show current time.\n"
            "3. Enter 'exit' to finish program.\n")
        try:
            if input_time == "":
                hh, mm = datetime.datetime.strftime(datetime.datetime.now(), '%I %M').split(" ")
            elif input_time.lower() == 'exit':
                exit("Program was finished by user.")
            else:
                hh, mm = input_time.split(':')

            if len(hh) == 2 and len(mm) == 2 and 0 <= int(hh) < 24 and 0 <= int(mm) <= 59:
                break
            else:
                raise Exception
        except Exception:
            print("Incorrect value! Try again.")

    hh = int(hh)
    mm = int(mm)

    if hh >= 12:
        hh = hh - 12

    if mm == 0:
        case_number = 0
    elif mm == 30:
        case_number = 1
    elif 1 <= mm <= 44:
        case_number = 2
    elif 45 <= mm <= 59:
        case_number = 3

    dict_hh_mm = {"0hh": ("Двенадцать", 3, "первого"),
                  "1hh": ("Один", 1, "второго"),
                  "2hh": ("Два", 2, "третьего"),
                  "3hh": ("Три", 2, "четвертого"),
                  "4hh": ("Четыре", 2, "пятого"),
                  "5hh": ("Пять", 3, "шестого"),
                  "6hh": ("Шесть", 3, "седьмого"),
                  "7hh": ("Семь", 3, "восьмого"),
                  "8hh": ("Восемь", 3, "девятого"),
                  "9hh": ("Девять", 3, "десятого"),
                  "10hh": ("Десять", 3, "одиннадцатого"),
                  "11hh": ("Одиннадцать", 3, "двенадцатого"),
                  "minutes": (("одна", 1), ("две", 2), ("три", 2), ("четыре", 2), ("пять", 3), ("шесть", 3),
                              ("семь", 3), ("восемь", 3), ("девять", 3), ("десять", 3), ("одиннадцать", 3),
                              ("двенадцать", 3), ("тринадцать", 3), ("четырнадцать", 3), ("пятнадцать", 3),
                              ("шестнадцать", 3), ("семнадцать", 3), ("восемнадцать", 3), ("девятнадцать", 3),
                              ("двадцать", 3), ("двадцать одна", 1), ("двадцать две", 2), ("двадцать три", 2),
                              ("двадцать четыре", 2), ("двадцать пять", 3), ("двадцать шесть", 3), ("двадцать семь", 3),
                              ("двадцать восемь", 3), ("двадцать девять", 3), ("половина", 0), ("тридцать одна", 1),
                              ("тридцать две", 2), ("тридцать три", 2), ("тридцать четыре", 2), ("тридцать пять", 3),
                              ("тридцать шесть", 3), ("тридцать семь", 3), ("тридцать восемь", 3),
                              ("тридцать девять", 3), ("сорок", 3), ("сорок одна", 1), ("сорок две", 2),
                              ("сорок три", 2), ("сорок четыре", 2), ("пятнадцати", 3), ("четырнадцати", 3),
                              ("тринадцати", 3), ("двенадцати", 3), ("одиннадцати", 3), ("десяти", 3),
                              ("девяти", 3), ("восьми", 3), ("семи", 3), ("шести", 3), ("пяти", 3),
                              ("четырех", 3), ("трех", 3), ("двух", 3), ("одной", 2)),
                  "hh_type": ("час", "часа", "часов"),
                  "mm_type": ("минута", "минуты", "минут")}

    if case_number == 0:
        hours_res = dict_hh_mm[str(hh) + 'hh'][0]
        hours_type = dict_hh_mm["hh_type"][dict_hh_mm[str(hh) + 'hh'][1] - 1]
        print(f"Your result:\t{' '.join([hours_res, hours_type]).capitalize()} ровно.\n")
    elif case_number in {1, 2}:
        hours_res = dict_hh_mm[str(hh) + "hh"][2]
        min_res = dict_hh_mm["minutes"][mm - 1][0]
        min_type = dict_hh_mm["mm_type"][dict_hh_mm["minutes"][mm - 1][1] - 1] if case_number == 2 else ""
        text_time = f"{min_res} {min_type} {hours_res}.".capitalize()
        print("Your result:\t", ' '.join(text_time.split()).strip() + "\n")
    else:
        hh = (hh + 1) if hh + 1 <= 11 else 0
        hours_res = dict_hh_mm[str(hh) + "hh"][0] if hh != 1 else "час"
        min_res = dict_hh_mm["minutes"][mm - 1][0]
        min_type = dict_hh_mm["mm_type"][dict_hh_mm["minutes"][mm - 1][1] - 1]
        text_time = f"Без {min_res} {min_type} {hours_res}.".capitalize()
        print("Your result:\t", ' '.join(text_time.split()).strip() + "\n")
