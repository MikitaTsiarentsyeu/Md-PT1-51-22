import os
import json

prefix = "eq_"
txt_ext = ".json"


def show_equipments(day_type):
    res = []
    directory = get_directory(day_type)
    for file_name in os.listdir(directory):
        if file_validation(file_name):
            with open(f"{directory}/{file_name}", 'r') as f:
                json_content = json.load(f)
                json_content.update({"file_name": convert_file_name(file_name)})
                res.append(json_content)
    return res


def get_directory(day_type=0):
    directory = "repo"
    if day_type == 1:
        directory = os.path.join("repo", "chest")
    elif day_type == 2:
        directory = os.path.join("repo", "hands")
    elif day_type == 3:
        directory = os.path.join("repo", "legs")
    elif day_type == 0:
        directory = [os.path.join(directory, i) for i in os.listdir(directory)]
    return directory


def file_validation(file_name):
    return file_name[-5:] == ".json"


def convert_file_name(file_name):
    return file_name[3:-5].lower().replace("_", " ")


def search_equipment(pattern):
    res = []
    for dir_name in get_directory(0):
        for filename in os.listdir(dir_name):
            if file_validation(filename):
                filename = convert_file_name(filename)
                if pattern in filename:
                    res.append(filename.capitalize())
    return res


def save_equipment(day_type, name, description, approaches_list):
    name = f"{prefix}{name.replace(' ', '_').lower()}{txt_ext}"
    name = os.path.join(get_directory(day_type), name)
    to_json = {"description": description, "approaches": approaches_list}
    with open(name, 'w') as f:
        json.dump(to_json, f)
        return True


# save_equipment(1, "Fly", "descr", {0: ['15', '35'], 1: ['15', '35'], 2: ['15', '35']})
# print(search_equipment("f"))
# print(show_equipments(1))