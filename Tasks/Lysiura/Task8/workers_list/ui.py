import bl



def add_user():
    name = bl.validate_name('name')
    surname = bl.validate_name('surname')
    date_of_birth = bl.validate_birth('date of birth')
    res = bl.add(name,surname, date_of_birth)
    if res:
        print("New user is added")
        print(res)
    else:
        print("Something went wrong")
    

def find_full_name_by_ID():
    id = bl.validate_id()
    res = bl.find_full_name_by_ID(id)
    if res:
        print("User's surname and name:")
        print(res)
    else:
        print("User is not found")
    


def show_user_info():
    id = bl.validate_id()
    res = bl.show_user_info(id)
    if res:
        print("Full info about user: ")
        print(res)
    else:
        print("User is not found")


def edit_user():
    ask = bl.validate_id()
    res = bl.edit_user(ask)
    if res:
       print("Information is changed")
    else:
        print("User is not found")
   

def delete():
    id = bl.validate_id()
    res = bl.delete(id)
    if res:
        print("User is deleted")
    else:
        print("User is not found")


def show_menu():
    while True:
        print("1. Add user")
        print("2. Find user's name and surname by ID")
        print("3. Show full users's info ")      
        print("4. Edit user's info")
        print("5. Delete user")
        print("6. Exit")
        
        choice = input("Choose any number: ")
        
        if choice == '1':
            add_user()
        elif choice == '2':
            find_full_name_by_ID()
        elif choice == '3':
            show_user_info()
        elif choice == '4':
            edit_user()
        elif choice == '5':
            delete()
        elif choice == '6':
            break
        else:
            print("Please choose a number from the list")
            continue


show_menu()