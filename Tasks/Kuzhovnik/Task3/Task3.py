var = [{"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
       "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
       "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20}, 0, list(), list()]

var[2] = input("Enter your numbers or press 'Enter' to use default numbers:\n").split(" ")
if var[2][0] == '':
       var[2] = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split(" ")
print(f"Your string: {var[2]}\n")

while var[1] < len(var[2]):
       var[3].append(var[0][var[2][var[1]]])
       var[1] += 1

print(f"From string to list: {var[3]}\n")
var = sorted(list(set(var[3])))
print(f"Sorted list without duplicates: {var}\n")
var.append(0)

while len(var) - 2 != var[-1]:
       if (var[-1] + 1) % 2 != 0:
              print(f"Product {var[-1] + 1} and {var[-1] + 2} numbers: {var[var[-1]] * (var[var[-1] + 1])}")
       else:
              print(f"Summ {var[-1] + 1} and {var[-1] + 2} numbers: {(var[var[-1]]) + (var[var[-1] + 1])}")
       var[-1] += 1
else:
       var[-1] = 0

var.append(0)

while len(var) - 2 != var[-2]:
       if var[var[-2]] % 2 != 0:
              var[-1] = var[-1] + var[var[-2]]
       var[-2] += 1
print("\nSum of all odd numbers: ", var[-1])
