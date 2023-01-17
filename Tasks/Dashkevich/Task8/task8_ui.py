import business_logic

def read_card():
    name = input("Please input name of card:\n")
    r = business_logic.read_card(name)
    if r:
        print("----------")
        print("Card name:", "card_" + name)
        print("Mr.Cardholder:", r[0])
        print("Phone:", r[1])
        print("Address:", r[2])
        print("----------")
    else:
        print("No 'business card' found by given name")

def add_card():
    name = input("Please, input parameter 'Card name':\n")
    cardholder = input("typing parameter 'Mr.Cardholder':\n")
    phone = input("typing parameter 'Phone':\n")
    address = input("typing parameter 'Address':\n")
    res = business_logic.add_card(name, cardholder, phone, address)
    if res:
        print("The 'business card' was added")
    else:
        print("'Business card' add is wrong")

def validate_name(ask="name"):
    while True:
        name = input(f"Please provide a {ask}:\n")
        try:
            if not name.replace(' ', '').isalnum():
                raise RuntimeError("Please use only alpha-numeric symbols")
            if len(name) > 40:
                raise RuntimeError("Please restrict the length of the name to a 40 symbols")
        except RuntimeError as e:
            print(e)
            continue
        else:
            break
    return name

def search_card():
    pattern = validate_name("query")
    res = business_logic.search_card(pattern)
    if res:
        print(f"'Business card' with this query in file name:")
        print(res)
    else:
        print(f"'Business card' with this query file name not found...")

def show_menu():
    while True:
        print("1. Read business card")
        print("2. Add new business card")
        print("3. Search business card")
        print("4. Exit")
        answer = input("Choose action:\n")
        if answer == "1":
            read_card()
        elif answer == "2":
            add_card()
        elif answer == "3":
            search_card()
        elif answer == "4":
            print('Goodbye!')
            break
        else:
            print("Please choose action number from this list...")
            continue

show_menu()