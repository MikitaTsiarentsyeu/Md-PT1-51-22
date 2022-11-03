num = input("Enter ONLY numbers: ")
chosen_hours = num.split(' ')

num_dict = {"one":1,"two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, 
            "eight":8, "nine":9, "ten":10,"eleven":11, "twelve": 12, "thirteen": 13,
            "fourteen": 14, "fifteen":15, "sixteen":16, "seventeen":17,
            "eighteen":18, "nineteen": 19, "twenty":20
                    }
i=0

new_dict = []
while i < len(chosen_hours):
    if chosen_hours[i] in num_dict:
        new_dict.append(num_dict[chosen_hours[i]])
        i+=1 
    else:
        print("Not correct values")
        break
sorted_list = sorted(list(set(new_dict)))
if len(sorted_list)>0:
        print(f"Sorted list: {sorted_list}") 
else:
    pass

mult_list = []
for z in range(len(sorted_list)-1):
    if z % 2 == 0:
        mult_list.append(sorted_list[z] * sorted_list[z+1])
print(f"Multiplication of numbers: {mult_list}")

sum_list = []
for z in range(len(sorted_list)-1):
    if z % 2 != 0:
        sum_list.append(sorted_list[z] + sorted_list[z+1])
print(f"Sum of numbers: {sum_list}")


sum_of_odd = 0
for i in sorted_list:
    if i%2!=0:
        sum_of_odd += i
print(f"Whole sum of odd numbers: {sum_of_odd} ")





