def check_str(string):
    upper_case = 0
    lower_case = 0
    for i in string:
        if i.isalpha():
            if i.islower():
                lower_case += 1
            else:  
                upper_case += 1  
    return(f'{upper_case} upper case, {lower_case} lower case')



          
str = 'The quick Brown Fox4R11 ddSS'
print(check_str(str))

