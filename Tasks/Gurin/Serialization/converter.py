import csv
import os
import json
import pickle

# each row as dict of lists
data_v1 = {"model":['80 1.6 Specs', '80 1.6 Specs'],"year":[1989, 1993],"horsepower":[69, 102],"engine size":[1595, 1595],} 

# each row as list of dicts
data_v2 = [
    {"model":"80 1.6 Specs", "year":"1989", "horsepower":"69", "engine size":"1595"},   
    {"model":"80 1.6 Specs", "year":"1993", "horsepower":"102", "engine size":"1595"}
]


absolute_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(absolute_path)

def dict_to_csv():
    with open("v1.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for i in range(len(data_v1[headline[0]])):
            row = []
            for key in headline:
                row.append(data_v1[key][i]) 
            writer.writerow(row)
pass


def list_to_csv():    
    with open("v2.csv", 'w', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames=headline)
        writer.writeheader()
        writer.writerows(data_v2)
pass


# Convert CSV to JSON (add headline) 
def convert_data1_csv_to_json():
    list = []
    with open("v1.csv", 'r') as f_csv:
        reader = csv.DictReader(f_csv, fieldnames=headline)
        for row in reader:
            list.append(row)

    with open("v1.json", 'w', newline='') as f_json:
            json_str = json.dumps(list, indent=4)
            f_json.write(json_str)   
pass

# Convert CSV to JSON
def convert_data2_csv_to_json():
    list = []
    with open("v2.csv", 'r', newline='') as f_csv:
        reader = csv.DictReader(f_csv)
        for row in reader:
            list.append(row)

    with open("v2.json", 'w', newline='') as f_json:
            json_str = json.dumps(list, indent=4)
            f_json.write(json_str)   
pass


# Convert JSON to Pickle 
def convert_data1_json_to_pickle():
    with open("v1.json", 'r') as f_json:
        res = json.load(f_json)
        
    with open("v1.pickle", 'wb') as f_pickle:
        pickle.dump(res, f_pickle)  
pass

# Convert JSON to Pickle 
def convert_data2_json_to_pickle():
    with open("v2.json", 'r') as f_json:
        res = json.load(f_json)
        
    with open("v2.pickle", 'wb') as f_pickle:
        pickle.dump(res, f_pickle)  
pass



headline = ["model","year","horsepower","engine size"]
dict_to_csv()
list_to_csv()
convert_data1_csv_to_json()
convert_data2_csv_to_json()
convert_data1_json_to_pickle()
convert_data2_json_to_pickle()