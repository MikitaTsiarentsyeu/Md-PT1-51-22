import json
import csv
import os


def save_camera(name, description):     
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(absolute_path)
    with open("camera_bd.csv", 'a+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, description])

def read_camera():
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(absolute_path)
    list = []
    with open("camera_bd.csv", 'r') as f:
        reader = csv.reader(f, quotechar='|')
        for row in reader:
            list.append(row)
    return list

def search(name): 
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(absolute_path)
    list = []
    with open("camera_bd.csv", 'r') as f:
        reader = csv.reader(f, quotechar='|')
        for row in reader:
            if row[0] == name:
                return row
            else:
                continue
        return    

if __name__ == "__main__":
    print("Please start with camera.py")