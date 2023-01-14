import os
prefix = "dieta_"
directory = os.path.join("dieta", "repo")
txt_ext = ".txt"

def save_receipe(name, content):
    name = f"{prefix}{name}.txt"
    name = os.path.join(directory, name)
    with open(name, 'w') as f:
        f.write(content)
        return True
    return False

def read_receipe(name):
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
    print("Please use book.py to start the app")