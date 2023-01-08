import os

prefix = "card_"
directory = os.path.join("console_app", "cards")
txt_extension = ".txt"

def save_card(name, content):
    name = f"{prefix}{name}.txt"
    name = os.path.join(directory, name)
    with open(name, 'w') as f:
        f.write(content)
        return True
    return False

def read_card(name):
    name = f"{prefix}{name}.txt"
    name = os.path.join(directory, name)
    with open(name, 'a+') as f:
        f.seek(0)
        return f.read()

def search_card(pattern):
    res = []
    for filename in os.listdir(directory):
        if txt_extension in filename:
            name = filename.replace(txt_extension, "")
            if pattern in name:
                res.append(name)
    return res