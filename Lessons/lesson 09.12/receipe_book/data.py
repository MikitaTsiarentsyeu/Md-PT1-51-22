import os
prefix = "receipe_"
directory = "receipe_book\\repo"

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
    with open(name, 'a+') as f:
        f.seek(0)
        return f.read()

def serach(pattern): pass

