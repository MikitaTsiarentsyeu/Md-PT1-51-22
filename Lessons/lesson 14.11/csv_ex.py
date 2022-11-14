import csv

fieldNames = ["make","model","cpu","gpu"]

with open("laptops.csv", 'r') as f:
    reader = csv.DictReader(f, fieldNames)
    for l in reader:
        print(l)

    # reader = csv.reader(f)
    # for l in reader:
    #     print(l)
    #     for elem in l:
    #         print(elem)

new_laptop = ['acer', 'helios', 'i5', 'rtx3050']
with open("laptops.csv", 'a', newline='') as f:
    writer = csv.DictWriter(f, fieldNames)

    writer.writerow({fieldNames[i]:new_laptop[i] for i in range(len(fieldNames))})

    # writer = csv.writer(f)
    # writer.writerow(new_laptop)

    


# skip = True

# makes, models = set(), set()

# with open("laptops.csv", 'r') as f:
#     for line in f:
#         if skip:
#             skip = False
#             continue
#         data = line.split(',')
#         makes.add(data[0])
#         models.add(data[1])

# print(makes, models)

# new_laptop = ['acer', 'predator', 'i7', 'rtx3080']
# with open("laptops.csv", 'a') as f:
#     f.write(','.join(new_laptop))