"""1. Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию
о количестве букв в верхнем и нижнем регистре.
check_str('The quick Brown Fox') -> '3 upper case, 13 lower case'

2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
is_prime(787) -> True
is_prime(777) -> False

3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
отсортированных по возрастанию, и которая этот список “сворачивает” в набор отрезков.

get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
get_ranges([4,7,10])  -> "4, 7, 10"
get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"""

def check_str(string) -> int:
    if isinstance(string, str):
        lower_char, upper_char = 0, 0
        for i in string:
            if i.islower():
                lower_char += 1
            elif i.isupper():
                upper_char += 1

        return [upper_char, lower_char]

def is_prime(number:int) -> bool:
    if number > 2 and number % 2 == 0:
        return False
    
    i = 2
    while number % i != 0:
        i+=1
        if i>=number:
            return True
    return False

def get_ranges(_list):
    _list = sorted(set(_list))
    if _list:
        temp_list = []
        result_list = []
        reversed_list = list(map(str, _list))
        for index, i in enumerate(reversed_list):
            if index == 0:
                 temp_list.append(reversed_list[index])
                 continue
             
            if int(i)-1 != int(reversed_list[index-1]):
                result_list.append(temp_list)
                temp_list = []
            temp_list.append(reversed_list[index])

        if temp_list:
            result_list.append(temp_list)
        
        for index, i in enumerate(result_list):
            del i[1:-1]

        result_string = ''
        for i in result_list:
            result_string += '-'.join(i) + ', '
        
        return result_string[:-2]
    

if __name__ == "__main__":
    string = 'The quick Brown Fox'
    print(f"{check_str(string)[0]} upper case, {check_str(string)[1]} lower case")
    print(is_prime(9))
    print(get_ranges([1,2,3,4,5,5,2,5,8,9,9,10]))
    print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
    print(get_ranges([4,7,10]))
    print(get_ranges([2, 3, 8, 9]))