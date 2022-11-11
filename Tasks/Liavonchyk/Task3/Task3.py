input_string, dict_string = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen', {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty'}

num_list = sorted([key for key, val in dict_string.items() if val in set(dict_string.values()).intersection(set(input_string.split(' ')))]) # used dict as I can't get list indexes in 1 line. Variable can be removed and the whole line may be used, but the code will be less readable

print([num_list[i] + num_list[i+1] if i % 2 == 1 else num_list[i] * num_list[i+1] for i in range(0, len(num_list) - 1) ]) # point 4
print(sum([key for key in num_list if key % 2 == 1])) # point 5

