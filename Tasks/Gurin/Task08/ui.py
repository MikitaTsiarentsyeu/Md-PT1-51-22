import bl


def read():
    print("List of all cameras:\n")
    cam = bl.read()
    print(cam)
    

def add(): 
    name = input("Please provide a name:\n")
    description = input("Please provide a description:\n")
    res = bl.add(name, description)
    if res:
        print("The camera was added")
    else:
        print("Something went wrong")


def search(): 
    name = input("Please provide a name:\n")
    res = bl.search(name)
    if res:
        print("The camera was found: ", res)
    else:
        print("The camera wasn't found")

def show_menu():
    while True:
        print("\nPlease choose option:\n")
        print("1. Read a camera")
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

show_menu()