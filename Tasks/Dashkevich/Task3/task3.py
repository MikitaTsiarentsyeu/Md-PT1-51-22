num_dict ={ "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
            "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
            "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, 
            "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20}
# user_numbers = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
user_numbers = input("Enter your numbers: ").split(" ")
list_no_duplicate, list_numbers, list_operations = [], [], []

for i in user_numbers:
    if i not in list_no_duplicate:
         list_no_duplicate.append(i)

for i in range(len(list_no_duplicate)):
    list_numbers.append(num_dict.get(list_no_duplicate[i]))

list_numbers = sorted(list_numbers)

for i in range(len(list_numbers)-1):
    if (i % 2) == 0:
         list_operations.append(list_numbers[i] * list_numbers[i+1])
    elif (i % 2) != 0:
        list_operations.append(list_numbers[i] + list_numbers[i+1])

sum_odd_numbers = 0
for i in range(len(list_numbers)):
    if list_numbers[i] % 2 != 0:
        sum_odd_numbers += list_numbers[i] 
       
print("Your numbers:", user_numbers)
print("List numbers without duplicate:", list_no_duplicate)
print("Sorted list:", list_numbers)
print("Products and additions:", list_operations)
print("Sum of odd numbers:", sum_odd_numbers)