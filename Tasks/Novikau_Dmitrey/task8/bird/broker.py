import data

def read():
    r = data.read_species()
    return r

def add(species, description):
    res = data.save_birdinfo(species, description)
    return res

def search(species):
    res = data.search(species)
    return res 

if __name__ == "__main__":
    print("Please use bird.py to start the app")