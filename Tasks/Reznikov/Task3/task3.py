import itertools

"""
Пользователь вводит строку, содержащую числительные через пробел, все числа больше 0 и меньше 21, например, 
“five thirteen two eleven seventeen two one thirteen ten four eight five nineteen”. 
Выполнить приведённые ниже действия для строки в общем виде, затратив минимальное количество строк кода:
- перейти от строки к списку целых чисел
- исключить дубликаты
- отсортировать по возрастанию
- вывести произведение первого и второго чисел, сумму второго и третьего, произведение третьего и четвёртого и т. д. (для коллекции любой длины)
- вывести полную сумму всех нечётных чисел
- использовать в программе только одну переменную (необязательная "задача со звёздочкой" поразвлекаться)
"""

def get_dict():
    x = {
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9,
        'ten':10,
        'eleven':11,
        'twelve':12,
        'thirteen':13,
        'fourteen':14,
        'fifteen':15,
        'sixteen':16,
        'seventeen':17,
        'eighteen':18,
        'nineteen':19,
        'twenty':20,
        'twenty one':21
    }
    return x

def get_odd_sum(x):
    return sum(filter(lambda x: (x%2 != 0) , get_array(x)))
    
def get_array(x):
    x = x.split(' ')
    x = [int(x) for x in x]
    return x

def get_multiply_result(x):
    return [x[0]*x[1] for x in itertools.zip_longest(
                                                [int(x[1]) for x in enumerate(get_array(x)) if int(x[0]) % 2 == 0],
                                                [int(x[1]) for x in enumerate(get_array(x)) if int(x[0]) % 2 != 0], 
                                                fillvalue=0)]
                                                

def get_sum_result(x):
    x = str([int(x[1]) for x in enumerate(get_array(x)) if int(x[0]) != 0]).replace('[', '').replace(']', '').replace(',', '')

    return [x[0]+x[1] for x in itertools.zip_longest(
                                                [int(x[1]) for x in enumerate(get_array(str(x))) if int(x[0]) % 2 == 0],
                                                [int(x[1]) for x in enumerate(get_array(str(x))) if int(x[0]) % 2 != 0], 
                                                fillvalue=0)]

def merge(x):
    return [x for x in zip([x for x in get_multiply_result(x)], [x for x in get_sum_result(x)]) for x in x]


x = [x.replace(x, f'{get_dict()[x]}') for x in input('Enter number: ').split(' ') if x in get_dict()]
x = list(set(x))
x = ' '.join(sorted(x, key=int))
print('New string: ' + x)
print(f'Sum odd numbers: {get_odd_sum(x)}')
print(f'Multiply and sum result: {merge(x)}')