dict_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
            "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
            "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20}

# text_num = "five thirteen two eleven five two fourteen twenty one"

# 1. go from a string to a list of integers
# 2. eliminate duplicates
# 3. sort ascending
num = sorted(set(dict_num[i] for i in input("Enter numbers:\n").split()))
print(num)

# 4. print the product of the 1st and 2nd numbers, the sum of the 2nd and 3rd, the product of the 3rd and 4th, etc.
for i in range(len(num)):
    if i == len(num) - 1:
        break
    else:
        print((num[i] * num[i + 1]) if (i + 1) % 2 != 0 else (num[i] + num[i + 1]), end=" ")
print()

# 5. print the total sum of all odd numbers
num = sum(filter(lambda i: i % 2 != 0, num))
print(num)
