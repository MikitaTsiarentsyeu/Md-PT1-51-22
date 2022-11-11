# One day there will be the only one variable in code but not today :)
num_dict = {'one': 1, 'two': 2, 'three': 3,
            'four': 4, 'five': 5, 'six': 6,
            'seven': 7, 'eight': 8, 'nine': 9,
            'ten': 10, 'eleven': 11, 'twelve': 12,
            'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
            'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
            'nineteen': 19, 'twenty': 20}
new_str = input('enter string with numerals separated by spaces\n').lower()

new_list = [num_dict[i] for i in new_str.split()]
print(new_list)


new_list = list(set(new_list))
print(new_list)


new_list = sorted(new_list)
print(new_list)


new_list = [new_list[i] * new_list[i+1] if i % 2 == 0 else new_list[i] + new_list[i+1] for i in range(len(new_list)-1)]
print(*new_list, sep=', ', end='.\n')


print(sum([i for i in new_list if i % 2 != 0]))


