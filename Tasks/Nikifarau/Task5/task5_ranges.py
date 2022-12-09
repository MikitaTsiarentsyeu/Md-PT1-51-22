def get_ranges(digital_list: list) -> str:
    start = 0
    result = ""
    len_of_list = len(digital_list)
    for list_index in range(len_of_list):
        if list_index == len_of_list - 1 or digital_list[list_index + 1] - digital_list[list_index] != 1:
            if list_index != start:
                result += f"{digital_list[start]}-{digital_list[list_index]}, "
            else:
                result += f"{digital_list[list_index]}, "
            start = list_index + 1
    return result[:-2]


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
