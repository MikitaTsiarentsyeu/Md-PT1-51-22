def check_str (str):
    counter_low = 0
    counter_up = 0
    for i in str:
        if i.islower():
            counter_low += 1
        elif i.isupper():
            counter_up += 1
        else:
            continue        
    print(f"{counter_up} upper case, {counter_low} lower case")        

def is_prime(num):
    if num > 0:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True        
    else:
        print("Please enter the number more than 0")

def get_ranges(list: list):
    list_temp = []
    counter = 0
    for i in range(len(list)-1):
        if i == 0:
            list_temp.append(f"{list[i]}")
        elif i == 1 and list[i] - list[i-1] == 1 and list[i+1] - list[i-1] != 2:
            list_temp.append(f"-{list[i]},")
        elif list[i+1] - list[i] == 1 and i == len(list)-2:
            list_temp.append(f" {list[i]}-{list[i+1]}")
        elif list[i+1] - list[i] == 1:
            counter += 1
        elif list[i+1] - list[i] > 1 and counter >= 1:
            list_temp.append(f"-{list[i]}, ")
            list_temp.append(f"{list[i+1]}")
            counter = 0
        elif list[i+1] - list[i] > 1:
            list_temp.append(f", {list[i]}, ")
            list_temp.append(f"{list[i+1]}")
        elif i == list[len(list)-2] and counter == 1:
            list_temp.append(f"{list[i]}")
    res = ''.join(list_temp)  
    return res

print(check_str('The quick Brown Fox'))

print(is_prime(787))
print(is_prime(777))

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))