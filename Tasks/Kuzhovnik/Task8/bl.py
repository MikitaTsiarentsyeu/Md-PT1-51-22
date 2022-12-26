import data


def show_equipments(day_type):
    res = data.show_equipments(day_type)
    appr_str = ""
    res_str = ""
    for i in range(len(res)):
        file_name = res[i]['file_name'].capitalize()
        short_descr = res[i]['description'][:70:]
        appr_str = "Set\t\tApproaches\tWage\nnumber\tcount\t\tvalue\n"
        for k_id in range(len(res[i]['approaches'])):
            appr_data = res[i]['approaches'][str(k_id)]
            appr_str += f"{k_id+1}\t\t{appr_data[0]}\t\t\t{appr_data[1]}\n"
        res_str += f"\nEquipment name: {file_name}\nShort description: {short_descr}..\n{appr_str}"
    return res_str


def search_equipment(pattern):
    res = data.search_equipment(pattern.lower())
    if res:
        return ', '.join(res)
    else:
        return ""


def add_equipment(day_type, name, description, approaches_list):
    for search_name in data.search_equipment(name):
        if search_name.lower() == name.lower():
            while True:
                try:
                    action = input("This name is already used.\n1. Rewrite\n2. Change name\n")
                    if action == "2":
                        name = input("Enter new name: ")
                        break
                    elif action != "1":
                        raise RuntimeError("Value error. Enter 1 or 2.")
                except RuntimeError as re:
                    print(re)
                break
    approaches_dict = {}
    for i in range(len(approaches_list)):
        approaches_dict[i] = approaches_list[i]
    res = data.save_equipment(day_type, name, description, approaches_dict)
    return "Gym equipment was added" if res else "Something went wrong"


if __name__ == "__main__":
    print("Please use gym_run.py to start the app")
