d = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
     'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
     'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
     'eighteen': 18, 'nineteen': 19, 'twenty': 20}
text = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'

l = list(set([d[i] for i in text.split()]))                                            #task123
print(l)

print(*[l[i] + l[i+1] if i%2 else l[i] * l[i+1] for i in range(len(l)-1) ], sep ='--')  #task4

print(sum([i for i in l if i%2]))                                                       #task5

