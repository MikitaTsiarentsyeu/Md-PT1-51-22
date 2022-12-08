big_and_small = input("Enter any string of text information:\n")


def check_str(big_and_small):
    counter_big = 0
    counter_small = 0
    for i in big_and_small:
        if i.isupper():
            counter_big += 1
        if i.islower():
            counter_small += 1
    return print(f"{counter_big} upper case, {counter_small} lower case")


check_str(big_and_small)
