import bl


def read():
    print("List of all cameras:\n")
    cam = bl.read()
    print(cam)
    

def add(): 
    name = validate_name()
    description = input("Please provide a description:\n")
    res = bl.add(name, description)
    if res:
        print("The camera was added")
    else:
        print("Something went wrong")


def search(): 
    name = validate_name("query")
    res = bl.search(name)
    if res:
        print("The camera was found: ", res)
    else:
        print("The camera wasn't found")

def show_menu():
    while True:
        print("1. List of all cameras")
        print("2. Add a camera")
        print("3. Search for a camera")
        print("4. Exit")
        answ = input("Choose your option:\n")
        if answ == "1":
            read()
        elif answ == "2":
            add()
        elif answ == "3":
            search()
        elif answ == "4":
            break
        else:
            print("Please make your choose")  
            continue  

def validate_name(ask="name"):
    while True:
        name = input(f"Please provide a {ask}:\n")
        try:
            if not name.replace(' ','').isalnum():
                raise RuntimeError("Please use only alpha-numeric symbols")
            if len(name) > 20:
                raise RuntimeError("Please restrict the length of the name to a 20 symbols")
        except RuntimeError as e:
            print(e)
        else:
            break
    return name

if __name__ == "__main__":
    show_menu()
    # print("Please start with camera.py")
