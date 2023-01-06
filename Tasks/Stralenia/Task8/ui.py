import bl
import const

def read():
    name = validate_name()
    r = bl.read(name)
    if r:
        print(name)
        print("Address:")
        print(r[0])
        print("Phonenamber:")
        print(r[1])
        
    else:
        print("No contect was found by given name")

def add():
    name = validate_name()
    address = input("Plese provide a address:\n")
    phonenamber = input("Plese provide a phonenamber:\n")
    res = bl.add(name, address, phonenamber)
    if res:
        print("The contect was added")
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
            
        except RuntimeError as e:
            print(e)
            continue
        else:
            break
    
    return name

def show_menu():

    while True:
        print("1. Read a contect")
        print("2. Add a contect")
        print("3. Search for a contect")
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