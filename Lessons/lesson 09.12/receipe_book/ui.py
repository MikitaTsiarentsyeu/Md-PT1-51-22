import bl

def read():
    name = input("Plese provide a name:\n")
    r = bl.read(name)
    if r:
        print(name)
        print("Ingrs:")
        print(r[0])
        print("Process:")
        print(r[1])
        print("--------------")
    else:
        print("Something went wrong")

def add():
    name = input("Plese provide a name:\n")
    ingrs = input("Plese provide a list of ingridients:\n")
    process = input("Plese provide a process:\n")
    res = bl.add(name, ingrs, process)
    if res:
        print("The receipe was added")
    else:
        print("Something went wrong")

def search(): pass

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

show_menu()