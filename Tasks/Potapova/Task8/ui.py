import bl
import os

def add_contact():
    name = validate_contact_info('name')
    number = validate_contact_info('number')
    if validate_chosen_pos(f'Are you sure you want to add the contact "name: {name}, number: {number}?(y\\n)\n', ['y', 'n']) == 'n':
        print('Adding contact was cancelled')
        return
    res = bl.add_contact(name, number)
    if res == 'dupl_error':
        print(f'Contact with the name "{name}" already exists')
    elif res == True:
        print(f'Contact "{name}" added to your phone book with number "{number}"')
    else:
        print('Something went wrong, please try again')
    """do not add empty"""


def delete_contact():
    name = validate_contact_info('name')
    parse_list, path_list = bl.view_contact_list(name)
    if parse_list:
        for el in parse_list:
            print(el)  # change to point
        chosen_contact_pos = int(validate_chosen_pos('Choose from list contact position you wish to delete\n', [str(i) for i in range(1, len(parse_list)+1)]))-1
        acc = validate_chosen_pos('Are you sure you want to delete this contact?(y\\n)\n', ['y', 'n'])
        if acc == 'y':
            if bl.delete_number(path_list[chosen_contact_pos]):
                print(f'Contact "{parse_list[chosen_contact_pos]}" was deleted from your phone book')
            else:
                print(f'Cannot delete contact file. It is opened somewhere else')
        else:
            print('Contact deletion was declined')
    else:
        print(f'There is no contacts with name "{name}" in your phone book')


def alter_number():
    name = validate_contact_info('name')
    parse_list, path_list = bl.view_contact_list(name)
    if parse_list:
        for el in parse_list:
            print(el)
        chosen_contact_pos = int(validate_chosen_pos('Choose from list contact position you wish to change.\n', [str(i) for i in range(1, len(parse_list)+1)]))-1
        for pos in range(len(bl.data_keys)):
            print(f'{pos + 1}. {bl.data_keys[pos]}')
        chosen_parameter = int(validate_chosen_pos('Choose from list parameter position you wish to change.\n', [str(i) for i in range(1, len(bl.data_keys)+1)]))-1
        new_value = validate_contact_info(f'new {bl.data_keys[chosen_parameter]}')
        res = bl.alter_number(new_value, path_list[chosen_contact_pos], bl.data_keys[chosen_parameter])
        while res != 'changed' and res != 'opened':
            res = bl.alter_number(new_value, path_list[chosen_contact_pos], bl.data_keys[chosen_parameter])
            if res == 'duplicate':
                print(f'Name "{new_value}" already exists, please try another name.\n')
                new_value = validate_contact_info(f'new {bl.data_keys[chosen_parameter]} please or press "q" to quit')
                if new_value.lower() == 'q':
                    print('Updating contact was cancelled')
                    return
        if res == 'opened':
            print('Cannot alter contact file. It is is opened somewhere else')
        print(
            f'Position {parse_list[chosen_contact_pos]} was altered. {bl.data_keys[chosen_parameter].capitalize()} was changed to {new_value}')
    else:
        print(f'There is no contacts with name "{name}" in your phone book')


def show_book():
    parse_list = bl.show_telephone_book()
    if parse_list:
        for el in parse_list:
            print(el)
    else:
        print('Your phone book is empty')


def search_number():
    name = validate_contact_info('name')
    parse_list = bl.search_numbers(name)
    if parse_list:
        for el in parse_list:
            print(el)
    else:
        print('There is no such contacts in your phone book')


def validate_contact_info(ask: str):
    while True:
        contact_info = input(f"enter {ask}:\n")
        try:
            if 'name' in ask:
                if not contact_info.replace(' ', '').replace("'", "").isalnum():
                    raise RuntimeError("Please use alpha-numeric symbols")
            elif 'number' in ask:
                if not contact_info.isdigit():
                    raise RuntimeError("Please use numeric symbols")
            if len(contact_info) > 20:
                raise RuntimeError("Please restrict the length of the name to a 20 symbols")
        except RuntimeError as e:
            print(e)
            continue
        else:
            break
    return contact_info


def validate_chosen_pos(question: str, choices_list):
    while True:
        chosen_pos = input(question).lower()
        try:
            if chosen_pos not in choices_list:
                raise RuntimeError("Incorrect input. Please try again")
        except RuntimeError as e:
            print(e)
            continue
        else:
            break
    return chosen_pos

def check_directory():
    if os.path.exists('repo'):
        return True
    else:
        try:
            os.mkdir('repo')
            return True
        except OSError:
            print ("Failed to create working directory")
            return False


def show_menu():
    print("Welcome to your phone book!")
    while check_directory():
        print("\n1. Add new contact")
        print("2. Delete contact")
        print("3. Update contact info")
        print("4. Search for contact")
        print("5. Look at whole book")
        print("6. Exit")
        answ = input("Please choose an option:\n")

        if answ == "1":
            add_contact()
        elif answ == "2":
            delete_contact()
        elif answ == "3":
            alter_number()
        elif answ == "4":
            search_number()
        elif answ == "5":
            show_book()
        elif answ == "6":
            print("Don't forget to recommend us to your friends :)\nGoodbye!")
            break
        else:
            print("Entered number is not correct. Try again:")
            continue




if __name__ == "__main__":
    show_menu()