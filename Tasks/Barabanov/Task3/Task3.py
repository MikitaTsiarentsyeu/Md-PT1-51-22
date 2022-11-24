dict = [
    {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
    },
    0,
    list(),
    list(),
]

dict[2] = input("Enter numbers or press 'Enter' to load default numbers:\n").split(
    " "
)
if dict[2][0] == "":
    dict[
        2
    ] = "ten thirteen nineteen two eleven seventeen two one five four eight five thirteen ".split(
        " "
    )
print(f"Your string: {dict[2]}\n")

while dict[1] < len(dict[2]):
    dict[3].append(dict[0][dict[2][dict[1]]])
    dict[1] += 1

print(f"From string to list: {dict[3]}\n")
dict = sorted(list(set(dict[3])))
print(f"Sorted list without duplicates: {dict}\n")
dict.append(0)

while len(dict) - 2 != dict[-1]:
    if (dict[-1] + 1) % 2 != 0:
        print(
            f"Product {dict[-1] + 1} and {dict[-1] + 2} numbers: {dict[dict[-1]] * (dict[dict[-1] + 1])}"
        )
    else:
        print(
            f"Sum {dict[-1] + 1} and {dict[-1] + 2} numbers: {(dict[dict[-1]]) + (dict[dict[-1] + 1])}"
        )
    dict[-1] += 1
else:
    dict[-1] = 0

dict.append(0)

while len(dict) - 2 != dict[-2]:
    if dict[dict[-2]] % 2 != 0:
        dict[-1] = dict[-1] + dict[dict[-2]]
    dict[-2] += 1
print("\nSum of all odd numbers: ", dict[-1])
