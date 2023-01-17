import broker

def read():
    print("All birds:\n")
    bird = broker.read()
    print(bird)

def add():     
    name = validate_name()
    description = input("Please provide a description:\n")
    res = broker.add(name, description)
    if res:
        print("The bird added")
    else:
        print("Sorry! Wrong")

def search():
    species = validate_name("query")
    res = broker.search(species)
    if res:
        print("The bird found: ", res)
    else:
        print("The bird wasn't found")

def validate_name(ask="species"):
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


def show_menu():
    while True:
        print("1.Read information about the bird")
        print("2.Add information about the bird")
        print("3.Search information about a bird")
        print("4.Exit")
        into = input("Choose point:\n")

        if into == "1":
            read()
        elif into == "2":
            add()
        elif into == "3":
            search()
        elif into == "4":
            break
        else:
            print("Choose point from menu!")

if __name__ == "__main__":
    show_menu()
