from itertools import zip_longest
dict_string = {0:1,1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty'}

# as we have a defined limit for length [1:20]
while dict_string[0] < 21:
    dict_string.pop(dict_string[0]) if dict_string[dict_string[0]] in set(dict_string.values()).difference(
        set('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split(' '))) else dict_string
    dict_string[0] = dict_string[0] + 1

print(list(dict_string.keys())[1:])

print(sum(list(set(dict_string.keys()).intersection({1,3,5,7,9,11,13,15,17,19}))))

dict_string = list(dict_string.keys())

dict_string[0] = 1
while dict_string[0] < len(dict_string) - 1:
    print(dict_string[dict_string[0]] * dict_string[dict_string[0] + 1] if dict_string[0] % 2 == 1 else dict_string[dict_string[0]] + dict_string[dict_string[0] + 1], end = ' ')
    dict_string[0] = dict_string[0] + 1

