def check_str(s):
    counter, counter2 = 0, 0
    for i in s:
        if i.isupper():
            counter += 1
        elif i.islower():
            counter2 +=1
        else:
            continue
    return print(f'{counter} upper case, {counter2} lower case')

s = 'The quick Brown Fox'
check_str(s)