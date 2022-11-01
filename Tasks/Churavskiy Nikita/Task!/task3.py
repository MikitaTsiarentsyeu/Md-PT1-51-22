number_values={ 
'one': 1, 'two': 2,'three': 3,'four':4,
'five': 5,'six': 6,'seven': 7,'eight': 8,
'nine': 9,'ten': 10,'eleven': 11, 'twelve': 12,
'thirteen': 13,'fourteen': 14,'fifteen': 15,'sixteen': 16,
'seventeen': 17,'eighteen': 18,'nineteen': 19,'twenty': 20
}

def decor(a):
    def wrapper():
        c = a()
        print(f"список введённых пользователем чисел - {sorted(c)}")
        print(f"значения без дубликатов и отсортированых по возрастанию - {sorted(set(c))}")
        try:
            print(f"произведение первого и второго чисел - {sorted(set(c))[0]*sorted(set(c))[1]}")
            print(f"сумма второго и третьего числа - {sorted(set(c))[1]+sorted(set(c))[2]}")
            print(f"произведение третьего и четвертого числа - {sorted(set(c))[2]*sorted(set(c))[3]}")
        except IndexError:
            print(f"Значения с таким индексом отсутсвует, проверьте правильность введенных данных")
        print(f"полная сумма всех нечетных чисел - {sum(set([i for i in c if i%2!=0]))}")
    return wrapper
   
@decor
def some_result():
    while True:
        enter_value = input("enter your values in range 1-21 (include 1 and include 21)\nin format 'five thirteen two eleven'\n" )
        list_number = [number_values[i] if i in number_values else 'not correctly' for i in enter_value.split()]
        if 'not correctly' in list_number:
            print(("not correctly format, please repeat\n"))
        else:
            return list_number

some_result()




