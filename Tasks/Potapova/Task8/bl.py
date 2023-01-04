import data

data_keys = ['name', 'number']

def add_contact(name: str, number: str):
    if data.duplicate_search(name):
        return 'dupl_error'
    else:
        return data.add_contact(name, number)


def view_contact_list(name: str):
    path_list = data.search_numbers_pattern(name)
    cont_info_list = data.show_contact_dict(path_list)
    if path_list:
        parse_list = data.parse_contact_dict(cont_info_list)
        return parse_list, path_list
    else:
        return [],[]


def delete_number(path_str: str):
    if data.delete_contact(path_str):
        return True
    else:
        return False


def alter_number(new_value, path_list, data_keys):
    if data_keys == 'name':
        if data.duplicate_search(new_value):
            return 'duplicate'
    if data.update_contact(path_list, data_keys, new_value):
        return 'changed'
    else:
        return 'opened'


def show_telephone_book():
    book = data.show_contact_dict(data.search_numbers_pattern(''))
    if book:
        return data.parse_contact_dict(book)
    else:
        return False


def search_numbers(name: str):
    contacts = data.show_contact_dict(data.search_numbers_pattern(name))
    if contacts:
        return data.parse_contact_dict(contacts)
    else:
        return False

