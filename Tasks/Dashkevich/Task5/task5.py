def check_str(user_string):
    
    upper_case_counter, lower_case_counter = 0, 0
    
    for i in user_string:
         if i.isupper() :
             upper_case_counter +=1
         if i.islower() :
             lower_case_counter +=1
    res = f"Your text contains {upper_case_counter} upper case, {lower_case_counter} lower case letters"
    return res

print('You can count letters in upper and lower case in this program')
user_string = input('Write your text, using upper and lower case: ')#"The quick Brown Fox"
print(check_str(user_string))

print("----------")

def is_prime(user_number):
    for i in range(2, user_number // 2):
        if (user_number % i) == 0:
            return False
        if user_number == 2:
            return True
    return True

print('You can check is your number - prime or not in this program')
user_number = int(input('Write your number: '))
print(is_prime(user_number))

print("----------")


def get_ranges(list_elements: list):
    result = ""
    i = 0
    result += str(list_elements[0])
    while i < len(list_elements):
        if i == len(list_elements)-1:
            return repr(result)
        else:
            i += 1
            if list_elements[i] - list_elements[i-1] == 1:
                if i == len(list_elements)-1:
                    if result[len(result) - 1] == "-":
                        pass
                    else:
                        result += "-"
                    result += str(list_elements[i])
                    return repr(result)
                else:
                    if list_elements[i+1] - list_elements[i] == 1:
                        if result[len(result) - 1] == "-":
                            continue
                        continue
                    if list_elements[i] - list_elements[i-1] == 1:
                        result += "-"

            elif list_elements[i] - list_elements[i-1] != 1:
                if i == len(list_elements)-1:
                    result += str(list_elements[i])
                    return repr(result)
                if i < len(list_elements)-1:
                    result += ", "
                    if list_elements[i+1] - list_elements[i] == 1:
                        result += str(list_elements[i+1])
                        i += 1
                        continue

            result += str(list_elements[i])
            result += ", "
            i += 1
            result += str(list_elements[i])
            continue

list_elements = [0, 1, 2, 3, 4, 7, 8, 10]
print(get_ranges(list_elements))
list_elements = [4, 7, 10]
print(get_ranges(list_elements))
list_elements = [2, 3, 8, 9]
print(get_ranges(list_elements))
list_elements = [1, 2, 3, 8, 9, 10, 12, 13, 25, 26, 27]
print(get_ranges(list_elements))