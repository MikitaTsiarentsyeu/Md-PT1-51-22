import csv
import os

# each row as dict of lists
data_v1 = {"model":['80 1.6 Specs', '80 1.6 Specs'],"year":[1989, 1993],"horsepower":[69, 102],"engine size":[1595, 1595],} 

# each row as list of dicts
data_v2 = [
    {"model":"80 1.6 Specs", "year":"1989", "horsepower":"69", "engine size":"1595"},   
    {"model":"80 1.6 Specs", "year":"1993", "horsepower":"102", "engine size":"1595"}
]
headline = ["model","year","horsepower","engine size"]

absolute_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(absolute_path)

with open("v1.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    for i in range(len(data_v1[headline[0]])):
        row = []
        for key in headline:
            row.append(data_v1[key][i]) 
        writer.writerow(row)

    
with open("v2.csv", 'w', newline = '') as f:
    writer = csv.DictWriter(f, fieldnames=headline)
    writer.writeheader()
    writer.writerows(data_v2)

