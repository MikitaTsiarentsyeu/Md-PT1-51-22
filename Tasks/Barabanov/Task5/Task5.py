# Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию
# о количестве букв в верхнем и нижнем регистре.
# check_str('The quick Brown Fox') -> '3 upper case, 13 lower case'
def check_str(string):
    if  len(string) != 0:
        lower = 0
        upper = 0
        for i in range(len(string)):
            if string[i].islower():
             lower += 1
            elif string[i].isupper():
                 upper += 1
        print(f"{upper} upper case, {lower} lower case")
    else:
        print("string is empty")

check_str("The quick Brown Fox")

# 2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True,
# если число является простым, и False, если нет.
# is_prime(787) -> True
# is_prime(777) -> False

def is_prime(val):
    if val > 0:
        count = 0
        for i in range(2, val // 2 + 1):
            if val % i == 0:
                count = count + 1
        if count <= 0:
            print(f"Result from {val}", end=": ")
            return True
        else:
            print(f"Result from {val}", end=": ")
            return False
    else:
        print("Val is less or equal zero")

print(is_prime(787))
print(is_prime(777))

# 3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, и которая этот список “сворачивает” в набор отрезков.
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

def get_ranges(list):
    res_list = []
    res_list.append([list[0]])
    for i in range(len(list) - 1):
        if list[i] + 1 == list[i + 1]:
            if len(res_list[len(res_list) - 1]) == 1:
                res_list[len(res_list) - 1].append(list[i + 1])
            else:
                res_list[len(res_list) - 1][1] = list[i + 1]
        elif list[i] + 1 != list[i + 1]:
            res_list.append([list[i + 1]])
    return (
        "".join(map(str, res_list))
        .replace(", ", "-")
        .replace("][", ", ")
        .replace("[", '"')
        .replace("]", '"')
    )

print(f"[0, 1, 2, 3, 4, 7, 8, 10] -> {get_ranges([0, 1, 2, 3, 4, 7, 8, 10])}")
print(f"[4,7,10] -> {get_ranges([4,7,10])}")
print(f"[2, 3, 8, 9] -> {get_ranges([2, 3, 8, 9])}")