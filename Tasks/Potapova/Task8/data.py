import json
import os
from pathlib import Path

encoding = 'UTF-8'
directory = os.path.abspath(os.path.join("repo"))
ext = '.json'


def add_contact(name: str, number: str) -> bool:
    """
    Creates a new json file with the name and number of the contact.
    Returns True on success, False otherwise.
    """
    try:
        with open(os.path.join(directory, f'{name.lower()}{ext}'), 'w', encoding=encoding) as f:
            print(json.dumps({"name": name, "number": number}), file=f, sep='\n')
            return True
    except FileNotFoundError:
        return False


def delete_contact(path: str) -> bool:
    """
    Deletes contact that already exist
    """
    try:
        os.remove(path)
        return True
    except PermissionError:
        return False


def update_contact(file_path: str, option: str, new_value: str) -> bool:
    """
    Changes chosen attributes of contact
    """
    with open(file_path, 'r', encoding=encoding) as rf:
        contact_dict = json.load(rf)
        contact_dict[option] = new_value
    try:
        with open(file_path, 'w', encoding=encoding) as wf:
            print(json.dumps(contact_dict), file=wf, sep='\n')
        if option == 'name':
            os.renames(file_path, os.path.join(directory, f'{contact_dict[option].lower()}{ext}'))
        return True
    except PermissionError:
        return False


def search_numbers_pattern(name: str) -> list:
    """search for contact returns path"""
    book = []
    contact_files = [i[2] for i in os.walk('repo')][0]
    for file in contact_files:
        if Path(file).suffix == ext:
            file_path = os.path.join(directory, f'{file}')
            if name.lower() in file.lower().replace(ext, ''):
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        contact_dict = json.load(f)
                        if contact_dict:
                            book.append(file_path)
                except Exception:
                    pass
    return book

def duplicate_search(name: str) -> bool:
    """search for contact returns path"""
    contact_files = [i[2] for i in os.walk('repo')][0]
    for file in contact_files:
        if Path(file).suffix == ext:
            if name.lower() == file.lower().replace(ext, ''):
                return True
    return False


def show_contact_dict(path_list: list) -> list:
    """shows contact info using path"""
    contact_info = []
    for file_path in path_list:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                contact_dict = json.load(f)
                if contact_dict:
                    contact_info.append(contact_dict)

        except Exception:
            pass
    return contact_info

def parse_contact_dict(contact_dict: list) -> list:
    parse_contact_list = []
    for pos in range(len(contact_dict)):
        s = ""
        if contact_dict[pos]:
            for key in contact_dict[pos]:
                s += f'{key}: {contact_dict[pos][key]}, '
            parse_contact_list.append(f'{pos + 1}. {s[:-2]}')
    return parse_contact_list



if __name__ == "__main__":
    print("Please use phone_book.py to start the app")