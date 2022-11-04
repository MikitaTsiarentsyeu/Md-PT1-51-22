input_string, even_sum , dict_string = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen', 0, {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty'}

num_list = sorted(list({key for key, val in dict_string.items() if val not in set(dict_string.values()).difference(set(input_string.split(' ')))}))

for i in range(0, num_list.__len__() - 1):
    print(num_list[i] + num_list[i+1], end = ' ') if i % 2 == 1 else print(num_list[i] * num_list[i+1], end = ' ')
    even_sum = even_sum + num_list[i] if num_list[i] % 2 == 1 else even_sum

print('\n', even_sum + num_list[len(num_list) - 1]) if num_list[len(num_list) - 1] % 2 == 1 else print('\n', even_sum)


#dict_string.__delitem__(tuple(set(dict_string.values()).difference(set('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split(' ')))))

#print(set(dict_string.values()).difference(set('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split(' '))))
# print(dict_string.keys(set(dict_string.values()).intersection(set('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split(' ')))))
# in_string = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split(' ')
# in_string = list(set(in_string))
# print(in_string)