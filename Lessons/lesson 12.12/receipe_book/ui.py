import bl
import const

def read():
    name = validate_name()
    r = bl.read(name)
    if r:
        print(name)
        print("Ingrs:")
        print(r[0])
        print("Process:")
        print(r[1])
        print("--------------")
    else:
        print("No receipe was found by given name")

def add():
    name = validate_name()
    ingrs = validate_separator("list of ingridients")
    process = validate_separator("process")
    res = bl.add(name, ingrs, process)
    if res:
        print("The receipe was added")
    else:
        print("Something went wrong")

def search():
    pattern = validate_name("query")
    res = bl.search(pattern)
    if res:
        print(res)
    else:
        print("Nothing was found")

def validate_name(ask="name"):
    while True:
        name = input(f"Please provide a {ask}:\n")
        try:
            if not name.replace(' ', '').isalnum():
                raise RuntimeError("Please use only alpha-numeric symbols")
            if len(name) > 20:
                raise RuntimeError("Please restrict the length of the name to a 20 symbols")
        except RuntimeError as e:
            print(e)
            continue
        else:
            break
    
    return name

def validate_separator(ask):
    while True:
        text = input(f"Plese provide a {ask}:\n")

        if const.SEP in text:
            print(f"Please do not use {const.SEP} symbols in your text")
            continue
        break

def show_menu():

    while True:
        print("1. Read a receipe")
        print("2. Add a receipe")
        print("3. Search for a receipe")
        print("4. Exit")
        answ = input("Choose your destiny:\n")

        if answ == "1":
            read()
        elif answ == "2":
            add()
        elif answ == "3":
            search()
        elif answ == "4":
            break
        else:
            print("Please choose a number from the list")
            continue



if __name__ == "__main__":
    show_menu()