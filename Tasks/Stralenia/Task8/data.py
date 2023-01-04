import os
prefix = "contect_"
directory = os.path.join("repo")
txt_ext = ".txt"

def save_contect(name, content):
    name = f"{prefix}{name}.txt"
    name = os.path.join(directory, name)
    with open(name, 'w') as f:
        f.write(content)
        return True
    return False

def read_contect(name):
    name = f"{prefix}{name}.txt"
    name = os.path.join(directory, name)
    try:
        with open(name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return False

def search(pattern):
    res = []
    for filename in os.listdir(directory):
        if txt_ext in filename:
            name = filename.replace(txt_ext, "")
            if pattern in name:
                res.append(name)
    return res

if __name__ == "__main__":
    print("Please use phonebook.py to start the app")