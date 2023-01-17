import os.path
import csv
{"species": "Merlin",
"description": "Falco"}

def save_birdinfo(species, description):
    way = os.path.dirname(bird.csv)
    os.chdir(way)
    with open("bird.csv", 'a', newline='') as f:
            writer_object = writer(f)
            writer_object.writerow([species, description])

def read_species(species):
    way = os.path.dirname(bird.csv)
    os.chdir(way)
    list = []
    with open("bird.csv", 'rb') as f:
        reader = csv.reader(f, quotechar='|')
        for row in reader:
            list.append(row)
    return list


def search(species):
    way = os.path.dirname(bird.csv)
    os.chdir(way)
    list = []
    with open("bird.csv", 'r') as f:
        reader = csv.reader(f, quotechar='|')
        for row in reader:
            if row[0] == species:
                return row
            else:
                continue
        return
    
if __name__ == "__main__":
    print("Please use bird.py to start the app")