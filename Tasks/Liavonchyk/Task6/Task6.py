def calc_array_sum(in_list):
    sum = 0 #counter
    def array_sum(in_list): #calc sum of level elements
        nonlocal sum
        for i in range(0, len(in_list)):
            if not isinstance(in_list[i], list):
                sum = sum + in_list[i]
            else:
                array_sum(in_list[i])
        return sum

    return array_sum(in_list)




def print_fibonacci(f_n):
    f_list = []
    #calculate fibonacci numbers
    def fibonacci(amount):
        if amount == 0:
            return 0
        elif amount == 1:
            return 0
        elif amount == 2:
            return 1
        else:
            return fibonacci(amount - 1) + fibonacci(amount - 2)
    #prepare a list of them
    for i in range (1, f_n + 1):
        f_list.append(fibonacci(i))
    return f_list


#test
print(print_fibonacci(10))
print(calc_array_sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))
print(calc_array_sum([1, 2, [2, 4, [[7, 8], 4, [6,8,[1,[2],3]]]]]))