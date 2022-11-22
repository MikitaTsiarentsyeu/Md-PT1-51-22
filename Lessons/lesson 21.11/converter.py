import csv

headline = ['model', 'year', 'horsepower', "engine size"]

data_v1 = {"model":["80 1.6 Specs", "80 1.6 Specs"], "year":[1989, 1993], "horsepower":[69, 102], "engine size":["1595 cm3", "1595 cm3"]}

data_v2 = [
    {headline[0]:"80 1.6 Specs", headline[1]:1989, headline[2]:69, headline[3]:"1595 cm3"},
    {headline[0]:"80 1.6 Specs", headline[1]:1993, headline[2]:102, headline[3]:"1595 cm3"}
]

with open("v2.csv", 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headline)
    writer.writeheader()
    writer.writerows(data_v2)

with open("v1,csv", 'w', newline='') as f:
    writer = csv.writer(f)
    for i in range(len(data_v1[headline[0]])):
        row = []
        for key in headline:
            row.append(data_v1[key][i])
        writer.writerow(row)