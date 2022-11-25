def check_str(s: str) -> str:
    """
    Function counts the number of uppercase and lowercase letters in a string
    :param s: str
    :return: str
    """
    res = {"upper_case": 0, "lower_case": 0}

    for i in s:
        if i.isupper():
            res["upper_case"] += 1
        elif i.islower():
            res["lower_case"] += 1

    return f'{res["upper_case"]} upper case, {res["lower_case"]} lower case'


# test = """A CSV file (Comma Separated Values file) is a type of plain text file that uses specific structuring to
# arrange tabular data."""
#
# print(check_str(test))

print("-------------------------------------------------------")


def is_prime(n: int) -> bool:
    """
    Function determines if a number is prime
    :param n: int, n > 0
    :return: bool
    """
    prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime = False
            break
        i += 1

    return prime
#
#
# print(is_prime(1), is_prime(777), is_prime(787))


print("-------------------------------------------------------")


def get_range(start: int, end: int) -> str:
    if start == end:
        return str(start)
    else:
        return f"{start}-{end}"


def get_ranges(elements: list) -> str:
    """
    Generates from a non-empty list of non-repeating integers, sorted in ascending order, a line of segments with a 
    step of 1
    :param elements: sorted list 
    :return: line of segments with a step of 1
    """
    start_value = elements[0]

    n = len(elements)

    res = []

    for i in range(n):
        element = elements[i]
        if i == n - 1:
            res.append(get_range(start_value, element))
            break

        next_element = elements[i + 1]
        if next_element - element != 1:
            res.append(get_range(start_value, element))
            start_value = next_element

    return ", ".join(res)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))

print("-------------------------------------------------------")
